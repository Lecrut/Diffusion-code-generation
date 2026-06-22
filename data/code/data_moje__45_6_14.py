from functools import reduce

def find_minimum(values):
    return reduce(lambda a, b: a if a < b else b, values)

if __name__ == '__main__':
    sample_list = [4, 1, 7, 3, 9, 2, 8]
    result = find_minimum(sample_list)
    print(result)