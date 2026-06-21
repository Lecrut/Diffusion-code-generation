class MaxFinder:
    def __init__(self, numbers):
        self._numbers = numbers

    @staticmethod
    def find_max(numbers):
        if not numbers:
            raise ValueError("The list of numbers is empty")
        max_value = numbers[0]
        for num in numbers[1:]:
            if num > max_value:
                max_value = num
        return max_value

if __name__ == '__main__':
    sample_numbers = [15, 8, 42, 3, 99, 27]
    finder = MaxFinder(sample_numbers)
    maximum_value = finder.find_max(finder._numbers)
    print(maximum_value)