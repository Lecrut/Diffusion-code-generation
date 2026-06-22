from functools import reduce
numbers = [3, 5, 2, 9, 1, 8, 6]

def get_max(arr):
    return reduce(lambda x, y: x if x > y else y, arr)

if __name__ == '__main__':
    print(get_max(numbers))