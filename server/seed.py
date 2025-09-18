from app import app, db
from models import Message

with app.app_context():
    print("🌱 Seeding database...")

    # Clear old data
    Message.query.delete()

    # Seed sample messages
    m1 = Message(body="Hello world!", username="Lucy")
    m2 = Message(body="Flask is awesome!", username="Angel")
    m3 = Message(body="React + Flask = ❤️", username="Dev")

    db.session.add_all([m1, m2, m3])
    db.session.commit()

    print("✅ Seeding complete!")
