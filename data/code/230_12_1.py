class ObjectLocker:
    def __init__(self, objects):
        self.objects = objects
    def log_all(self):
        for obj in self.objects:
            print(f"Logging object: {obj}")
if __name__ == '__main__':
    sample_data = [1, 2, 3, "hello", 5.5]
    locker = ObjectLocker(sample_data)
    locker.log_all()