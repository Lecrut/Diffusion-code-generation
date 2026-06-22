def calculate_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("Length2 cannot be zero.")
    return length1 / length2

if __name__ == '__main__':
    length1 = 10.5
    length2 = 3.2
    try:
        ratio = calculate_ratio(length1, length2)
        print(f"The ratio of {length1} to {length2} is {ratio:.10f}")
    except ValueError as e:
        print(e)