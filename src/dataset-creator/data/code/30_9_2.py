import json
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None
    tags: List[str] = []
def parse_json_to_object(json_str: str) -> Any:
    try:
        data = json.loads(json_str)
        if isinstance(data, dict):
            return User(**data)
        elif isinstance(data, list):
            items = [User(**item) for item in data]
            return items
        raise ValueError("Invalid JSON structure")
    except Exception as e:
        print(f"Validation Error: {e}")
        raise
if __name__ == '__main__':
    sample_data = '{"id": 1, "name": "Alice", "email": "alice@example.com", "age": 30}'
    parsed_user = parse_json_to_object(sample_data)
    print(f"ID: {parsed_user.id}")
    print(f"Name: {parsed_user.name}")
    print(f"Email: {parsed_user.email}")
    print(f"Age: {parsed_user.age}")