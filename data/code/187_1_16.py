class MaxFinder:
    MAX_START = float('-inf')

    @staticmethod
    def find_max(numbers):
        if not numbers:
            return None
        largest = MaxFinder.MAX_START
        for number in numbers:
            if number > largest:
                largest = number
        return largest

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2, 9, 4]
    max_finder = MaxFinder()
    print(max_finder.find_max(sample_values))