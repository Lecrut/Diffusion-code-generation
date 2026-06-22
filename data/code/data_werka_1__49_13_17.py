def validate_lengths(length1, length2):
    if length1 == 0 or length2 == 0:
        raise ValueError("Lengths cannot be zero")

def calculate_ratio(length1, length2):
    validate_lengths(length1, length2)
    ratio = length1 / length2 if length1 > length2 else length2 / length1
    return round(ratio, 10)

if __name__ == '__main__':
    length1 = 27.5
    length2 = 5.3
    result = calculate_ratio(length1, length2)
    print(result)