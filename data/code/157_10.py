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
    input_list = [34, 12, 56, 9, 88, 23, 10]
    result = find_smallest(input_list)
    print(result)