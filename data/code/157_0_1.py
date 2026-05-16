import math
def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)
if __name__ == '__main__':
    numbers = [3, 1, 4, 1, 5, 9, 2]
    smallest = find_smallest(numbers)
    print(smallest)