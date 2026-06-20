def calculate_length_ratio(length1, length2):
    smallest = min(length1, length2)
    largest = max(length1, length2)
    return largest / smallest

if __name__ == '__main__':
    l1 = 10.0
    l2 = 5.0
    result = calculate_length_ratio(l1, l2)
    print(result)