from functools import reduce

class MaxFinder:
    @staticmethod
    def find_max(numbers):
        return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    max_value = MaxFinder.find_max(sample_values)
    print(max_value)