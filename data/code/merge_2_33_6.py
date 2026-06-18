class LogChecker:
    def __init__(self):
        self.registered_ids = {"user_001", "admin_x9"}
    def is_registered(self, identifier: str) -> bool:
        return identifier in self.registered_ids
if __name__ == '__main__':
    checker = LogChecker()
    test_cases = ["user_002", "admin_x9", "guest_temp"]
    for case in test_cases:
        result = checker.is_registered(case)
        print(f"{case}: {result}")