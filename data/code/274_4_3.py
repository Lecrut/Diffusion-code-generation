class DataProcessor:
    def __init__(self, data):
        self.data = data
    def print_all(self):
        for item in self.data:
            print(item)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    processor = DataProcessor(sample_list)
    processor.print_all()