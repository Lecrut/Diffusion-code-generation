class LogSystem:
    def is_registered(self, identifier):
        registered_ids = ["user123", "admin_01"]
        return identifier in registered_ids
if __name__ == '__main__':
    log_system = LogSystem()
    test_id = "user456"
    result = log_system.is_registered(test_id)
    print(result)