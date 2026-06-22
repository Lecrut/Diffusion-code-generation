from functools import reduce

def find_minimum(lst):
    if not lst:
        return None
    return reduce(lambda x, y: x if x < y else y, lst)

if __name__ == '__main__':
    sample_data = [34, 15, 88, 2, 57, 91, 10]
    result = find_minimum(sample_data)
    print(result)