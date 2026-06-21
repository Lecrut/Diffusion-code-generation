from functools import reduce

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return reduce(lambda x, y: x if x < y else y, data)

if __name__ == '__main__':
    sample_list = [5, 3, 9, 1, 10]
    print(find_minimum(sample_list))