class MaxFinder:
    DEFAULT_MAX = float('-inf')

    @staticmethod
    def find_max(numbers):
        if not numbers:
            return None
        current_max = MaxFinder.DEFAULT_MAX
        for number in numbers:
            if number > current_max:
                current_max = number
        return current_max
if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 30, 1]
    result = MaxFinder.find_max(sample_numbers)
    print(result)