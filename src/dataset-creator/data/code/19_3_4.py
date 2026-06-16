import json
from dataclasses import dataclass
@dataclass
class User:
    id: int
    name: str
    email: str
    age: int
def generate_data():
    users = [
        User(id=1, name="Alice", email="alice@example.com", age=30),
        User(id=2, name="Bob", email="bob@example.com", age=25),
        User(id=3, name="Charlie", email="charlie@example.com", age=40)
    ]
    return users
def transform_to_json(users):
    data = {
        "total_users": len(users),
        "users": [
            {"id": u.id, "name": u.name, "email": u.email, "age": u.age} 
            for u in users
        ],
        "average_age": sum(u.age for u in users) // len(users) if users else 0
    }
    return json.dumps(data, indent=2)
if __name__ == '__main__':
    raw_data = generate_data()
    output_json = transform_to_json(raw_data)
    print(output_json)