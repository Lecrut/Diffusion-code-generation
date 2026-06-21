class LargestNumberFinder:
    @staticmethod
    def find_largest(numbers):
        if not numbers:
            return None
        largest = numbers[0]
        for number in numbers[1:]:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_numbers = [15, 8, 22, 4, 30, 11]
    result = LargestNumberFinder.find_largest(sample_numbers)
    print(result)
    empty_list = []
    result_empty = LargestNumberFinder.find_largest(empty_list)
    print(result_empty)