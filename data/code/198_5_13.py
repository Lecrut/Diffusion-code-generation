class MinFinder:
    EMPTY_LIST_ERROR = 'List is empty'

    @staticmethod
    def find_absolute_minimum(numbers):
        if not numbers:
            raise ValueError(MinFinder.EMPTY_LIST_ERROR)
        min_value = numbers[0]
        for number in numbers:
            if number < min_value:
                min_value = number
        return min_value
if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 7]
    try:
        result = MinFinder.find_absolute_minimum(sample_list)
        print(result)
    except ValueError as e:
        print(e)