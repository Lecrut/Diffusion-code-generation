from functools import reduce

def find_minimum(lst):
    if not lst:
        return None
    return reduce(lambda a, b: a if a < b else b, lst)

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 57, 99, 12]
    result = find_minimum(sample_list)
    print(result)