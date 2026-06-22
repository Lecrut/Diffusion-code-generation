def compare_lengths(length1, length2):
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    length_a = 150
    length_b = 200
    result = compare_lengths(length_a, length_b)
    print(result)