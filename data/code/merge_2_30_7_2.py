import dataclasses
from typing import Any
class SchemaValidator:
    def validate(self, obj_class: type, instance_data: dict[str, Any]) -> None:
        for field in dataclasses.fields(obj_class):
            expected_type = field.type if not isinstance(field.type, (list, set)) else list(field.type)
            value = instance_data.get(field.name)
            if value is None and field.default_factory == dataclasses.MISSING:
                raise ValueError(f"Required argument '{field.name}' missing for {obj_class.__name__}")
            if expected_type != Any and not isinstance(value, expected_type):
                raise TypeError(f"Argument '{field.name}' must be of type {expected_type}, got {type(value).__name__}")
@dataclasses.dataclass
class User:
    id: int = dataclasses.field(default=0)
    name: str = ""
    email: str = "unknown@example.com"
    def __init__(self, **kwargs):
        validator = SchemaValidator()
        try:
            validator.validate(User, kwargs)
            object.__setattr__(self, 'id', kwargs.get('id', User.id))
            object.__setattr__(self, 'name', kwargs.get('name', User.name))
            object.__setattr__(self, 'email', kwargs.get('email', User.email))
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid initialization for {User.__name__}: {e}")
if __name__ == '__main__':
    user = User(id=123, name="Alice", email="alice@example.com")
    print(user.id, user.name, user.email)