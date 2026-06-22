from functools import reduce

def get_max_value(arr):
    return reduce(lambda a, b: a if a > b else b, arr)

if __name__ == '__main__':
    print(get_max_value([3, 1, 4, 1, 5, 9, 2, 6]))