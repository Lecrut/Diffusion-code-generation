def calculate_ratio(length1, length2):
    if length1 == 0 or length2 == 0:
        raise ValueError("Lengths cannot be zero")
    ratio = length1 / length2
    return ratio

if __name__ == '__main__':
    sample_length1 = 15.5
    sample_length2 = 7.25
    try:
        result_ratio = calculate_ratio(sample_length1, sample_length2)
        print(f"The ratio of {sample_length1} to {sample_length2} is: {result_ratio:.10f}")
    except ValueError as e:
        print(e)