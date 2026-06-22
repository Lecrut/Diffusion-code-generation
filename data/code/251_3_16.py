class DetermineTheLargestNumberPresentProcessor:
    def __init__(self):
        self.data = []

    def update_data(self, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        self.data.extend(numbers)

    def get_largest_number(self):
        if not self.data:
            raise ValueError("No data available to determine the largest number")
        return max(self.data)

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    processor.update_data([10, 5, 20, 8, 15])
    print(f"Largest number: {processor.get_largest_number()}")

    processor.update_data([-5, -1, -10, -3])
    print(f"Largest number after update: {processor.get_largest_number()}")