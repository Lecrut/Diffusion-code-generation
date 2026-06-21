from functools import reduce

def find_smallest(data):
    if not data:
        return None
    return reduce(lambda a, b: a if a < b else b, data)

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3, 7]
    print(find_smallest(sample_list))