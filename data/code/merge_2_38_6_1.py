import re
def sanitize_string(value: str) -> str:
    return value.strip() if isinstance(value, str) else ""
class SecureDictionary:
    def __init__(self):
        self._data = {}
    def add_entry(self, key: object, value: object) -> None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        sanitized_key = sanitize_string(str(key))
        sanitized_value = sanitize_string(value)
        self._data[sanitized_key] = sanitized_value
    def get_entry(self, key: object) -> str | None:
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        return self._data.get(sanitize_string(str(key)))
if __name__ == '__main__':
    secure_dict = SecureDictionary()
    sample_entries = [
        ("user_name", "Alice"),
        ("email_address", "alice@example.com"),
        ("full_name", "A. Smith")
    ]
    for key, value in sample_entries:
        try:
            secure_dict.add_entry(key, value)
        except TypeError as e:
            print(f"Error adding entry {key}: {e}")
    print("Secure Dictionary Contents:")
    for k, v in sorted(secure_dict._data.items()):
        print(f"{k!r} -> {v!r}")