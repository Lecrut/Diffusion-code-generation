class LargestNumberFinder:
    MAX_INT = float('-inf')

    @staticmethod
    def find_largest(numbers):
        if not numbers:
            return None
        largest = LargestNumberFinder.MAX_INT
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_numbers = [15, 8, 22, 4, 30, 11]
    finder = LargestNumberFinder()
    result = finder.find_largest(sample_numbers)
    print(result)

    empty_list = []
    result_empty = finder.find_largest(empty_list)
    print(result_empty)