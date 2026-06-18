import json
from pydantic import BaseModel, ValidationError
class User(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        extra = 'ignore'
def parse_json_to_object(json_str: str) -> dict:
    try:
        data = json.loads(json_str)
        if not isinstance(data, dict):
            raise ValidationError("Input must be a JSON object")
        return {k: v for k, v in data.items()}
    except Exception as e:
        print(f"Validation Error: {e}")
        return None
if __name__ == '__main__':
    sample_data = '{"id": 123, "name": "Alice", "email": "alice@example.com"}'
    result = parse_json_to_object(sample_data)
    if result is not None:
        print("Parsed Data:", json.dumps(result))
        try:
            validated_user = User(**result)
            print("Validated Schema Check Passed")
            print(f"ID Type: {type(validated_user.id).__name__}")
            print(f"Name Length: {len(validated_user.name)}")
        except ValidationError as ve:
            print(f"Simplified Pydantic Validation Failed: {ve.errors()}")