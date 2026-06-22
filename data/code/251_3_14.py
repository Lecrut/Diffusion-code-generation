class DetermineTheLargestNumberPresentProcessor:
    def __init__(self):
        self.data = []

    def update_data(self, number):
        if isinstance(number, (int, float)):
            self.data.append(number)

    def get_largest_number(self):
        return max(self.data) if self.data else None

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    processor.update_data(10)
    processor.update_data(20)
    processor.update_data(5)
    print(processor.get_largest_number())