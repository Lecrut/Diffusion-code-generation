class LogSystem:
    def is_registered(self, identifier):
        registered_ids = ["user_123", "admin_456"]
        return identifier in registered_ids
if __name__ == '__main__':
    log_system = LogSystem()
    test_cases = [
        ("user_123"),
        ("guest_789"),
        ("system_log")
    ]
    for case in test_cases:
        result = log_system.is_registered(case[0])
        print(f"Identifier '{case[0]}': {'Registered' if result else 'Not Registered'}")