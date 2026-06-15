class DataProcessor:
    def __init__(self):
        self.data = [10, 20, 30, 40, 50]
    def print_all_contents(self):
        for item in self.data:
            print(item)
if __name__ == '__main__':
    processor = DataProcessor()
    processor.print_all_contents()