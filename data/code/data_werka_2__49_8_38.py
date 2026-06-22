def compare_lengths(length1, length2):
    min_length = length1 if length1 < length2 else length2
    max_length = length1 if length1 > length2 else length2
    return (min_length, max_length)

if __name__ == '__main__':
    first_length = 35
    second_length = 40
    result = compare_lengths(first_length, second_length)
    print(result)