from dataclasses import dataclass, field
import json
@dataclass(frozen=True)
class User:
    id: int = field(default=0)
    name: str = ""
    email: str = ""
    def __post_init__(self):
        if not isinstance(self.id, (int, float)):
            raise TypeError("id must be numeric")
        if len(self.name.strip()) == 0 or self.name[0].isupper() != True:
            raise ValueError("name must start with a capital letter and cannot be empty after stripping")
        if "@" not in self.email:
            raise ValueError("email must contain an '@' symbol")
def validate_user(data):
    try:
        return User(**data)
    except (TypeError, ValueError) as e:
        print(f"Validation error for {type(e).__name__}: {e}")
        return None
if __name__ == '__main__':
    valid_data = {"id": 101, "name": "Alice Smith", "email": "alice@example.com"}
    invalid_name_data = {"id": 102, "name": "bob smith", "email": "bob@test.org"}
    result_valid = validate_user(valid_data)
    print(f"Valid User: {result_valid}")
    result_invalid = validate_user(invalid_name_data)