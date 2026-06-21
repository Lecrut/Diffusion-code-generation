from functools import reduce

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return reduce(lambda x, y: x if x < y else y, data)

if __name__ == '__main__':
    sample_list = [34, 78, 12, 56, 90, 23, 67]
    print(find_minimum(sample_list))