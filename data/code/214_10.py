import math
def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for x in data:
        if x < smallest:
            smallest = x
    return smallest
if __name__ == '__main__':
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_smallest(numbers)
    print(result)