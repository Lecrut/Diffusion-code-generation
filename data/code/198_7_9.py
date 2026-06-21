from functools import reduce

class MinFinder:
    MIN_VALUE = float('inf')

    @staticmethod
    def find_smallest(data):
        if not data:
            return None
        return reduce(lambda x, y: x if x < y else y, data, MinFinder.MIN_VALUE)

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3, 7]
    min_value = MinFinder.find_smallest(sample_list)
    print(min_value)