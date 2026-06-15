import sys
def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] > largest:
            largest = data[i]
    return largest
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    result = find_largest(sample_list)
    print(result)