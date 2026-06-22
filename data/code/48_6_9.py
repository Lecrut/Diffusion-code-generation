import operator

def find_max(nums):
    return functools.reduce(operator.gt, nums, nums[0])

if __name__ == '__main__':
    import functools
    values = [10, 45, 3, 22, 99, 12]
    result = find_max(values)
    print(result)