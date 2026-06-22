import sys

class MinFinder:
    _DEFAULT_EMPTY_SENTINEL = None

    @staticmethod
    def get_minimum(integers):
        if not integers:
            return MinFinder._DEFAULT_EMPTY_SENTINEL
        return min(integers)

if __name__ == '__main__':
    test_data = [102, 45, 3, 88, 15, 0, -5]
    minimum_value = MinFinder.get_minimum(test_data)
    print(minimum_value)