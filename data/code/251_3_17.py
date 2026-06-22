class DetermineTheLargestNumberPresentProcessor:
    def __init__(self):
        self.data = []

    def update_data(self, new_data):
        if not new_data:
            raise ValueError("Input list cannot be empty")
        self.data.extend(new_data)

    def get_largest_number(self):
        if not self.data:
            raise ValueError("No data available to determine the largest number")
        return max(self.data)

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    sample_data1 = [10, 5, 20, 8, 15]
    sample_data2 = [-5, -1, -10, -3]
    sample_data3 = [42]

    processor.update_data(sample_data1)
    print(f"Largest number in {sample_data1}: {processor.get_largest_number()}")

    processor.update_data(sample_data2)
    print(f"Largest number in {sample_data2}: {processor.get_largest_number()}")

    processor.update_data(sample_data3)
    print(f"Largest number in {sample_data3}: {processor.get_largest_number()}")