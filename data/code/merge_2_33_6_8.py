class LogRegistry:
    def __init__(self):
        self._registered_ids = set()
    def register(self, identifier: str) -> None:
        if not isinstance(identifier, str):
            raise TypeError("Identifier must be a string.")
        self._registered_ids.add(identifier.lower())
    def is_registered(self, identifier: str) -> bool:
        return identifier.lower() in self._registered_ids
if __name__ == '__main__':
    registry = LogRegistry()
    test_identifiers = ["user_123", "admin_user", "guest"]
    to_register = ["USER_456", "ADMIN_USER", "GUEST"]
    for id in to_register:
        registry.register(id)
    checks = [
        ("user_123", True),
        ("admin_user", True),
        ("unknown_id", False),
        ("USER_456", True),                          
    ]
    for identifier, expected in checks:
        result = registry.is_registered(identifier)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{identifier}' is registered? {result}")