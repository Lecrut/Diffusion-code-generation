from functools import reduce

def find_smallest(data):
    if not data:
        return None
    smallest = reduce(lambda x, y: x if x < y else y, data)
    return smallest

if __name__ == '__main__':
    sample_list = [4, 2, 9, 1, 5, 6]
    result = find_smallest(sample_list)
    print(result)