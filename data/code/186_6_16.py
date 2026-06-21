class SortedGenerator:
    def __init__(self, items):
        self.items = sorted(items)
    
    def get_next(self):
        return next(iter(self.items), None)

if __name__ == '__main__':
    sample_data = ["banana", "apple", "cherry", "date", "elderberry"]
    sg = SortedGenerator(sample_data)
    while True:
        item = sg.get_next()
        if item is None:
            break
        print(item, end=' ')