class MaxFinder:
    @staticmethod
    def find_max_value(numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        return max(numbers)

if __name__ == '__main__':
    finder = MaxFinder()
    print(finder.find_max_value([3, 1, 4, 1, 5, 9, 2]))
    print(finder.find_max_value([-10, -5, -20, -1]))
    print(finder.find_max_value([7]))
    try:
        print(finder.find_max_value([]))
    except ValueError as e:
        print(e)