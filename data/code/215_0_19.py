class LargestNumberFinder:
    @staticmethod
    def find_largest_number(numbers):
        if not numbers:
            raise ValueError("Input list is empty")
        return max(numbers)

if __name__ == '__main__':
    input_data = [10, 5, 20, 3, 15]
    try:
        largest_number = LargestNumberFinder.find_largest_number(input_data)
        print(largest_number)
    except ValueError as e:
        print(e)