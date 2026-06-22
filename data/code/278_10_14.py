class ListProcessor:
    def __init__(self, data):
        self.data = data

    def print_items(self):
        for item in self.data:
            print(item)

if __name__ == '__main__':
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        123,
        "Date"
    ]
    processor = ListProcessor(sample_items)
    processor.print_items()