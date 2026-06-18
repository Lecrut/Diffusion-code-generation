class SystemLogChecker:
    def is_registered(self, identifier):
        registered_ids = {"user_123", "admin_root", "service_bot"}
        return identifier in registered_ids
if __name__ == '__main__':
    checker = SystemLogChecker()
    test_id = "unknown_user"
    result = checker.is_registered(test_id)
    print(f"{test_id} is {'registered' if result else 'not registered'}")