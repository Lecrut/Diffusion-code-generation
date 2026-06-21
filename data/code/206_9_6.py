from functools import reduce

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return reduce(lambda x, y: x if x < y else y, data)

if __name__ == '__main__':
    sample_list = [34, 12, 98, 23, 56, 78, 11]
    print(f"Minimum element found: {find_minimum(sample_list)}")