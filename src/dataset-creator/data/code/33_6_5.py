class SystemLogChecker:
    def __init__(self):
        self.registered_ids = {"user_123", "admin_bot", "guest_user"}
    def is_registered(self, identifier: str) -> bool:
        return identifier in self.registered_ids
if __name__ == '__main__':
    checker = SystemLogChecker()
    test_cases = ["user_456", "admin_bot", "system_core"]
    for id_val in test_cases:
        result = checker.is_registered(id_val)
        print(f"ID {id_val}: {'Registered' if result else 'Not Registered'}")