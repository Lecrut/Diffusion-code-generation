def find_length_ratio(length1, length2):
    smallest = min(length1, length2)
    largest = max(length1, length2)
    ratio = largest / smallest
    return ratio

if __name__ == '__main__':
    first_length = 7
    second_length = 14
    length_ratio = find_length_ratio(first_length, second_length)
    print(length_ratio)