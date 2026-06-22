from functools import reduce

def max_via_reduce(arr):
    return reduce(lambda a, b: a if a > b else b, arr)

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6]
    result = max_via_reduce(sample_array)
    print(result)