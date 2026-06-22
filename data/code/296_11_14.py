def calculate_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    return f"{numerator}:{denominator}"

if __name__ == '__main__':
    result = calculate_ratio(3, 4)
    print(result)