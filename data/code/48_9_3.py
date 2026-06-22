from functools import reduce

def max_via_reduce(arr):
    return reduce(lambda a, b: a if a > b else b, arr)

if __name__ == '__main__':
    sample = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(max_via_reduce(sample))