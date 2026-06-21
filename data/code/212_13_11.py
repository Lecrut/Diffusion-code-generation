class MinMaxFinder:
    @staticmethod
    def find_min_max(numbers):
        if not numbers:
            return None
        minimum = min(numbers)
        maximum = max(numbers)
        return (minimum, maximum)

if __name__ == '__main__':
    sample_list = [10, 4, 25, 8, 30, 15]
    result = MinMaxFinder.find_min_max(sample_list)
    print(result)