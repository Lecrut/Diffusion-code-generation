def calculate_ratio(numerator, denominator):
    return f"{numerator}:{denominator}"

if __name__ == '__main__':
    ratio1 = 6
    den1 = 9
    result1 = calculate_ratio(ratio1, den1)
    print(f"Ratio: {ratio1}/{den1}, Result: {result1}")
    ratio2 = 10
    den2 = 15
    result2 = calculate_ratio(ratio2, den2)
    print(f"Ratio: {ratio2}/{den2}, Result: {result2}")