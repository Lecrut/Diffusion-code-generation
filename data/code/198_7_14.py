from functools import reduce

SMALLEST = float('inf')

def find_smallest(data):
    return reduce(lambda x, y: x if x < y else y, data, SMALLEST)

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3, 7]
    print(find_smallest(sample_list))