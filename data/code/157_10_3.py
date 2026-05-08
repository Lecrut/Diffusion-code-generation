import sys
def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for x in data[1:]:
        if x < smallest:
            smallest = x
    return smallest
if __name__ == '__main__':
    input_list = [3, 1, 4, 1, 5, 9, 2, 8]
    result = find_smallest(input_list)
    print(result)