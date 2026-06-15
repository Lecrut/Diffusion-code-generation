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
    numbers = [15, 3, 8, 22, 1, 45, 9]
    result = find_smallest(numbers)
    print(result)