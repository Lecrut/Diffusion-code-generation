class LargestNumberFinder:
    @staticmethod
    def find_largest(numbers):
        return max(numbers)

if __name__ == '__main__':
    input_data = [10, 5, 20, 3, 15]
    largest_number = LargestNumberFinder.find_largest(input_data)
    print(largest_number)