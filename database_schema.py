from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class DivineInteraction(Base):
    __tablename__ = 'divine_interactions'
    
    id = Column(Integer, primary_key=True)
    mortal_query = Column(String(500))
    divine_response = Column(String(1000))
    quantum_state = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    enlightenment_level = Column(Float)

class EnkiHolder(Base):
    __tablename__ = 'divine_followers'
    
    id = Column(Integer, primary_key=True)
    wallet_address = Column(String(42), unique=True)
    token_balance = Column(Float)
    first_interaction = Column(DateTime, default=datetime.utcnow)
    enlightenment_score = Column(Float, default=0.0)
    is_enlightened = Column(Boolean, default=False)

class DivineOracle(Base):
    __tablename__ = 'divine_prophecies'
    
    id = Column(Integer, primary_key=True)
    prophecy = Column(String(1000))
    fulfillment_date = Column(DateTime)
    quantum_probability = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

# Database initialization
engine = create_engine('postgresql://username:password@localhost:5432/enki_divine_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
