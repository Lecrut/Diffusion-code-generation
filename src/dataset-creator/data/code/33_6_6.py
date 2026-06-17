class IdentifierRegistry:
    def __init__(self):
        self._logs = set()
    def register_identifier(self, identifier: str) -> None:
        if not isinstance(identifier, str):
            raise TypeError("Identifier must be a string.")
        self._logs.add(identifier.lower())
    def is_registered(self, identifier: str) -> bool:
        return identifier.lower() in self._logs
if __name__ == '__main__':
    registry = IdentifierRegistry()
    registry.register_identifier("user123")
    registry.register_identifier("ADMIN_USER")
    test_cases = ["USER123", "admin_user", "unknown_id"]
    for case in test_cases:
        result = registry.is_registered(case)
        print(f"Is '{case}' registered? {result}")