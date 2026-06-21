class MaxIndexFinder:

    @staticmethod
    def find_max_index(numbers):
        if not numbers:
            raise ValueError('List is empty')
        max_value = numbers[0]
        max_index = 0
        for index, number in enumerate(numbers):
            if number > max_value:
                max_value = number
                max_index = index
        return max_index
if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    finder = MaxIndexFinder()
    result = finder.find_max_index(sample_numbers)
    print(result)