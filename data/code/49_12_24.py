def calculate_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("The denominator cannot be zero.")
    return length1 / length2

if __name__ == '__main__':
    LENGTH1 = 15.75
    LENGTH2 = 3.25
    try:
        ratio = calculate_ratio(LENGTH1, LENGTH2)
        print(f"The ratio of {LENGTH1} to {LENGTH2} is: {ratio:.10f}")
    except ValueError as e:
        print(e)