from functools import reduce
numbers = [3, 5, 2, 9, 1, 7]
def get_max_value(nums):
    return reduce(lambda a, b: a if a > b else b, nums)
if __name__ == '__main__':
    print(get_max_value(numbers))