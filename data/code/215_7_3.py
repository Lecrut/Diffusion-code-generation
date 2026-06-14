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
    test_list_small = [10, 5, 20, 8]
    print(find_largest(test_list_small))
    test_list_large = [999999999999999999999, 123456789012345678901, 555555555555555555555]
    print(find_largest(test_list_large))
    test_list_neg = [-10, -5, -20]
    print(find_largest(test_list_neg))