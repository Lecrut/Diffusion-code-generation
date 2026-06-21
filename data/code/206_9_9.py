import functools

class MinimumFinder:
    MIN_VALUE = float('inf')

    @staticmethod
    def reduce_minimum(data):
        return functools.reduce(lambda acc, x: acc if acc < x else x, data, MinimumFinder.MIN_VALUE)

if __name__ == '__main__':
    sample_list = [34, 2, 1, 78, 90, 56]
    min_value = MinimumFinder.reduce_minimum(sample_list)
    print(f"Minimum value in the list: {min_value}")