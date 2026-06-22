TOLERANCE = 10

def compare_lengths(length_a: int, length_b: int) -> bool:
    return abs(length_a - length_b) <= TOLERANCE

if __name__ == '__main__':
    sample_length_1 = 250
    sample_length_2 = 245
    result = compare_lengths(sample_length_1, sample_length_2)
    print(result)