class LogChecker:
    def is_registered(self, identifier):
        registered_ids = ["user_123", "admin_456", "guest_789"]
        return identifier in registered_ids
if __name__ == '__main__':
    checker = LogChecker()
    test_id = "unknown_user"
    result = checker.is_registered(test_id)
    print(result)