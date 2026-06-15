import math
def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for x in data[1:]:
        if x < smallest:
            smallest = x
    return smallest
if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 9]
    result = find_smallest(sample_list)
    print(result)