from functools import reduce

class MaxFinder:
    @staticmethod
    def find_max(numbers):
        return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    max_value = MaxFinder.find_max(sample_numbers)
    print(max_value)