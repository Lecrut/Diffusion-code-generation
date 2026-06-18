class SystemLogger:
    def is_registered(self, identifier):
        registered_ids = ["user_123", "admin_user", "service_bot"]
        return identifier in registered_ids
if __name__ == '__main__':
    logger = SystemLogger()
    test_cases = [
        ("unknown_id", False),
        ("user_123", True),
        ("new_admin", False)
    ]
    for ident, expected in test_cases:
        result = logger.is_registered(ident)
        print(f"Identifier '{ident}': Registered={result}, Expected={expected}")