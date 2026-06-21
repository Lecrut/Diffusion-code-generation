import math

def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    values = [56, 34, 21, 98, 17, 4]
    smallest_value = find_smallest(values)
    print(smallest_value)