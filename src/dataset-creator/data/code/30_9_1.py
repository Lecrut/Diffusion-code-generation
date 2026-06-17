import json
from pydantic import BaseModel, ValidationError
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None
def parse_json_to_objects(json_str: str) -> list[User]:
    try:
        data = json.loads(json_str)
        if not isinstance(data, list):
            raise ValidationError("Input must be a JSON array")
        objects = []
        for item in data:
            user_obj = User(**item)
            objects.append(user_obj)
        return objects
    except (json.JSONDecodeError, ValidationError) as e:
        print(f"Validation Error: {e}")
        raise
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "name": "Alice", "email": "alice@example.com"},
        {"id": 102, "name": "Bob", "age": 30},
        {"id": 103, "name": "Charlie", "email": "charlie@test.org"}
    ]
    json_string = json.dumps(sample_data)
    try:
        parsed_users = parse_json_to_objects(json_string)
        for user in parsed_users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    except Exception as e:
        pass