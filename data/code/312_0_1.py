import random
def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    return largest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_largest(sample_list)
    print(result)