class DetermineTheLargestNumberPresentProcessor:
    def __init__(self):
        self.data = {}

    def update_data(self, key, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        self.data[key] = max(numbers)

    def get_largest_number(self, key):
        return self.data.get(key, None)

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    processor.update_data('list1', [10, 5, 20, 8, 15])
    processor.update_data('list2', [-5, -1, -10, -3])
    processor.update_data('list3', [42])
    
    print(f"Largest number in list1: {processor.get_largest_number('list1')}")
    print(f"Largest number in list2: {processor.get_largest_number('list2')}")
    print(f"Largest number in list3: {processor.get_largest_number('list3')}")