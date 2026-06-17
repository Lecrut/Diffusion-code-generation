import json
from dataclasses import dataclass, field
@dataclass
class User:
    id: int
    name: str = ""
    email: str | None = None
    active: bool = True
    metadata: dict[str, any] = field(default_factory=dict)
def serialize_user(user: User, default_value=None):
    return {k: v for k, v in user.__dict__.items() if v is not None or (not isinstance(v, type(None)) and len(str(v).strip()) > 0)}
if __name__ == '__main__':
    users = [
        User(id=1, name="Alice", email=None),
        User(id=2, name="", active=False),
        User(id=3)
    ]
    serialized_data = []
    for user in users:
        data = serialize_user(user)
        if not any(v is None or v == "" for v in data.values()):
            serialized_data.append(data)
    json_str = json.dumps(serialized_data, indent=2)