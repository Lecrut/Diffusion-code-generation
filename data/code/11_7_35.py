def calculate_length_ratio(length1, length2):
    if length2 == 0:
        raise ValueError('length2 cannot be zero')
    numerator = length1
    denominator = length2
    ratio = numerator / denominator
    return ratio
if __name__ == '__main__':
    sample_length1 = 25.6
    sample_length2 = 4.0
    try:
        result_ratio = calculate_length_ratio(sample_length1, sample_length2)
        print(result_ratio)
    except ValueError as e:
        print(e)