from functools import reduce

def find_smallest(data):
    if not data:
        return None
    return reduce(lambda x, y: x if x < y else y, data)

if __name__ == '__main__':
    sample_list = [34, 78, 12, 56, 90, 23, 67]
    smallest_value = find_smallest(sample_list)
    print(smallest_value)