def compare_lengths(length1, length2):
    return max(length1, length2)

if __name__ == '__main__':
    first_length = 45.6
    second_length = 38.9
    longer_dimension = compare_lengths(first_length, second_length)
    print(longer_dimension)