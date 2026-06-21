from functools import reduce

def find_minimum(data):
    return reduce(lambda x, y: x if x < y else y, data)

if __name__ == '__main__':
    sample_list = [34, 78, 12, 90, 56]
    print(find_minimum(sample_list))