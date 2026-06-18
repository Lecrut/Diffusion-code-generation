import json
from pydantic import BaseModel, ValidationError
class User(BaseModel):
    id: int
    name: str
    email: str
    age: float | None = None
def parse_json_to_struct(data: dict) -> User:
    try:
        return data.model_dump()
    except Exception as e:
        raise ValidationError.from_exception_data("root", [e]) from e
if __name__ == '__main__':
    sample_input = {
        "id": 123,
        "name": "Alice Smith",
        "email": "alice@example.com"
    }
    try:
        result = parse_json_to_struct(sample_input)
        print(json.dumps(result))
    except Exception as e:
        print(f"Validation failed: {e}")