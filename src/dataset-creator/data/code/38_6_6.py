import re
def sanitize_string(value: str) -> str:
    return value.strip() if isinstance(value, str) else ""
class SecureDictionary:
    def __init__(self):
        self._data = {}
    def add(self, key: object, value: object) -> None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        sanitized_key = sanitize_string(str(key))
        sanitized_value = sanitize_string(value)
        self._data[sanitized_key] = sanitized_value
    def get(self, key: object) -> str | None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        return self._data.get(sanitize_string(str(key)), "")
if __name__ == '__main__':
    secure_dict = SecureDictionary()
    secure_dict.add("username", "admin_user_123")
    secure_dict.add("password_hash", "$2b$10$rNt9...hashed_value_here...")
    print(f"Username: {secure_dict.get('username')}")
    try:
        insecure_key = 12345
        result = secure_dict.get(insecure_key)
    except TypeError as e:
        print(f"Error caught: {e}")