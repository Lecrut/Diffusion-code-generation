from functools import reduce

def find_minimum(lst):
    if not lst:
        raise ValueError("List must not be empty")
    return reduce(lambda x, y: x if x < y else y, lst)

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 45, 16, 9]
    result = find_minimum(sample_list)
    print(result)