import re

_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

def validate_email(email: str) -> bool:
    return isinstance(email, str) and _PATTERN.match(email) is not None

if __name__ == "__main__":
    result = validate_email("user@example.com")
    print(result)