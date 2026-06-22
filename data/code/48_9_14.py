from functools import reduce

def find_max(arr):
    return reduce(lambda a, b: a if a > b else b, arr)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    print(find_max(sample_data))