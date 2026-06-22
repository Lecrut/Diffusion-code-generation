class DetermineTheLargestNumberPresentProcessor:
    def __init__(self):
        self.data = []

    def add_numbers(self, numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be numbers")
        self.data.extend(numbers)

    def get_largest_number(self):
        if not self.data:
            raise ValueError("No data to determine the largest number")
        return max(self.data)

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    processor.add_numbers([10, 5, 20, 8, 15])
    processor.add_numbers([-5, -1, -10, -3])
    processor.add_numbers([42])
    try:
        print(f"Largest number: {processor.get_largest_number()}")
    except ValueError as e:
        print(e)