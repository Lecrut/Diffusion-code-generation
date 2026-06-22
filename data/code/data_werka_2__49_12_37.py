def calculate_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("The denominator length cannot be zero.")
    return length1 / length2

if __name__ == '__main__':
    LENGTH_1 = 17.25
    LENGTH_2 = 4.25
    try:
        ratio = calculate_ratio(LENGTH_1, LENGTH_2)
        print(f"The ratio of {LENGTH_1} to {LENGTH_2} is: {ratio:.10f}")
    except ValueError as e:
        print(e)