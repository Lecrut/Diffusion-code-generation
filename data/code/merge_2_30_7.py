import dataclasses
from typing import Any
class SchemaValidator:
    def validate(self, obj_type: type, **kwargs) -> None:
        required_fields = getattr(obj_type, '__dataclass_fields__', {})
        if not required_fields:
            return
        for field_name in required_fields.keys():
            expected_value = kwargs.get(field_name)
            field_info = required_fields[field_name]
            annotation = field_info.type
            if not isinstance(expected_value, (annotation)):
                raise ValueError(f"Field '{field_name}' must be of type {annotation.__name__}, got {type(expected_value).__name__}")
            is_numeric = hasattr(annotation, '__origin__') and annotation in (int, float)
            if isinstance(expected_value, int) and field_name == "id":
                pass                   
        return
@dataclasses.dataclass
class User:
    id: int
    name: str
    email: str
    def __post_init__(self):
        validator = SchemaValidator()
        try:
            validator.validate(User, **vars(self))
        except ValueError as e:
            raise type(e)(f"Initialization failed for {type(self).__name__}: {e}")
def create_user(id_val: int, name_str: str, email_str: str) -> User:
    return User(id=id_val, name=name_str, email=email_str)
if __name__ == '__main__':
    valid_user = create_user(101, "Alice Johnson", "alice@example.com")
    print(f"Created user: {valid_user}")
    try:
        invalid_user = User(id="not_a_number", name="Bob", email="bob@test.org")
    except ValueError as e:
        print(f"Caught expected error for validation failure: {e}")