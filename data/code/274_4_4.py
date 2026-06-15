class DataProcessor:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]
    def print_all_contents(self):
        for item in self.data:
            print(item)
if __name__ == '__main__':
    processor = DataProcessor()
    processor.print_all_contents()