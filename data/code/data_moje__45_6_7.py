from functools import reduce

def find_min(values):
    if not values:
        raise ValueError("List must not be empty")
    return reduce(lambda x, y: x if x < y else y, values)

if __name__ == '__main__':
    sample_list = [5, 3, 8, 1, 9, 2]
    result = find_min(sample_list)
    print(result)