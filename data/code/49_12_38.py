def calculate_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("Length2 cannot be zero.")
    return length1 / length2

if __name__ == '__main__':
    sample_length1 = 25.456789
    sample_length2 = 7.345678
    try:
        ratio_result = calculate_ratio(sample_length1, sample_length2)
        print(f"The ratio of {sample_length1} to {sample_length2} is: {ratio_result:.10f}")
    except ValueError as e:
        print(e)