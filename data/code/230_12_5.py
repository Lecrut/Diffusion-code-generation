class ObjectLocker:
    def __init__(self, items):
        self.items = items
    def log_all(self):
        for item in self.items:
            print(f"Logging object: {item}")
if __name__ == '__main__':
    sample_data = [10, 25, 42, 99]
    locker = ObjectLocker(sample_data)
    locker.log_all()