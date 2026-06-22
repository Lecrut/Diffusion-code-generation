class DetermineTheLargestNumberPresentProcessor:
    def __init__(self):
        self.data = []

    def add_data(self, number):
        if not isinstance(number, (int, float)):
            raise ValueError("Input must be a number")
        self.data.append(number)

    def get_largest_number(self):
        if not self.data:
            return None
        return max(self.data)

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    processor.add_data(10)
    processor.add_data(5)
    processor.add_data(20)
    processor.add_data(8)
    processor.add_data(15)
    print(f"Largest number: {processor.get_largest_number()}")