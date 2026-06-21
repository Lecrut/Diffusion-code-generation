class LargestNumberFinder:
    @staticmethod
    def find_largest_number(numbers):
        return max(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    largest_number = LargestNumberFinder.find_largest_number(sample_values)
    print(largest_number)