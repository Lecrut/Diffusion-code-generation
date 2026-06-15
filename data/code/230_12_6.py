class ObjectLocker:
    def __init__(self, items):
        self.items = items
    def log_all_items(self):
        for item in self.items:
            print(f"Logging object: {item}")
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    locker = ObjectLocker(sample_data)
    locker.log_all_items()