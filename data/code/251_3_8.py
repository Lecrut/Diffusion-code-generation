class DetermineTheLargestNumberPresentProcessor:
    def __init__(self):
        self.data = {}

    def update_data(self, key, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        maximum = max(numbers)
        self.data[key] = maximum

    def get_largest_number(self, key):
        return self.data.get(key, None)

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    processor.update_data('sample1', [10, 5, 20, 8, 15])
    processor.update_data('sample2', [-5, -1, -10, -3])
    processor.update_data('sample3', [42])
    print(f"Largest number in sample1: {processor.get_largest_number('sample1')}")
    print(f"Largest number in sample2: {processor.get_largest_number('sample2')}")
    print(f"Largest number in sample3: {processor.get_largest_number('sample3')}")