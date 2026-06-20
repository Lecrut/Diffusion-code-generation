def calculate_length_difference(length_a, length_b):
    return length_a - length_b if length_a > length_b else length_b - length_a

if __name__ == '__main__':
    sample_length_1 = 10
    sample_length_2 = 4
    result = calculate_length_difference(sample_length_1, sample_length_2)
    print(result)