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
        parsed_users = []
        for item in data:
            user = User(**item)
            parsed_users.append(user)
        return parsed_users
    except (json.JSONDecodeError, ValidationError) as e:
        print(f"Validation Error: {e}")
        raise
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "age": 30},
        {"invalid_field": True}
    ]
    json_string = json.dumps(sample_data)
    try:
        users = parse_json_to_objects(json_string)
        for user in users:
            print(f"User ID: {user.id}, Name: {user.name}")
    except Exception as e:
        pass