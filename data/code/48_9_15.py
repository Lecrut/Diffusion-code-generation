from functools import reduce

def get_max_with_reduce(arr):
    return reduce(lambda a, b: a if a > b else b, arr)

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(get_max_with_reduce(sample_array))