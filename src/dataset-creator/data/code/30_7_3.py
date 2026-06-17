import dataclasses
from typing import Any
class SchemaValidator:
    def validate(self, obj_class: type[Any], instance_data: dict[str, Any]) -> None:
        for field in dataclasses.fields(obj_class):
            expected_type = field.type
            if not isinstance(instance_data.get(field.name), expected_type):
                raise TypeError(f"Field '{field.name}' must be of type {expected_type}, got {type(instance_data.get(field.name))}")
@dataclasses.dataclass
class User:
    name: str
    age: int
    email: str
if __name__ == '__main__':
    validator = SchemaValidator()
    try:
        user_instance = User(name="Alice", age=30, email="alice@example.com")
        print(f"Created valid object: {user_instance}")
        invalid_data = {"name": "Bob", "age": "thirty", "email": "bob@test.org"}
        validator.validate(User, invalid_data)
    except TypeError as e:
        print(f"Validation failed with error: {e}")