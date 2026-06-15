class ObjectLister:
    def __init__(self, objects):
        self.objects = objects
    def print_all(self):
        for obj in self.objects:
            print(f"Object details: {obj}")
if __name__ == '__main__':
    sample_data = [
        "Apple",
        "Banana",
        "Cherry",
        "Date"
    ]
    lister = ObjectLister(sample_data)
    lister.print_all()