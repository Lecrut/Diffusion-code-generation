from functools import reduce
def find_max(nums):
    return reduce(lambda a, b: a if a > b else b, nums)
if __name__ == '__main__':
    data = [12, 45, 3, 89, 23, 67, 99, 10]
    print(find_max(data))