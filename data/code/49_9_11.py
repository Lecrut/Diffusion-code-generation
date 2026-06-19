def compare_lengths(length1, length2):
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    SAMPLE_LENGTH_1 = 50
    SAMPLE_LENGTH_2 = 30
    result = compare_lengths(SAMPLE_LENGTH_1, SAMPLE_LENGTH_2)
    print(result)