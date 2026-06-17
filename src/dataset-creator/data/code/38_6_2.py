import re
def sanitize_string(value: str) -> str:
    return value.strip() if isinstance(value, str) else ""
class SecureDictionary:
    def __init__(self):
        self._data = {}
    def add(self, key: object, value: object) -> None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        sanitized_key = sanitize_string(str(key))
        sanitized_value = sanitize_string(value)
        self._data[sanitized_key] = sanitized_value
    def get(self, key: object) -> object | None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        return self._data.get(sanitize_string(str(key)))
if __name__ == '__main__':
    secure_dict = SecureDictionary()
    sample_data = [
        ("username", "admin_user"),
        ("password_hash", "$2b$10$r7k...secure_hash_here..."),
        ("email", "user@example.com")
    ]
    for k, v in sample_data:
        secure_dict.add(k, v)
    print(secure_dict.get("username"))