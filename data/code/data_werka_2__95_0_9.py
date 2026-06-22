def validate_number(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")
    if isinstance(n, float) and n != int(n):
        raise ValueError("Input must be an integer")
    return int(n)

def analyze_properties(number):
    validated = validate_number(number)
    is_positive = validated > 0
    is_even = validated % 2 == 0
    is_divisible_by_three = validated % 3 == 0
    return {
        "value": validated,
        "positive": is_positive,
        "even": is_even,
        "divisible_by_three": is_divisible_by_three
    }

if __name__ == '__main__':
    sample_values = [12, 7, -6, 15, 0]
    for val in sample_values:
        result = analyze_properties(val)
        print(f"{result['value']}: {result['positive']}, {result['even']}, {result['divisible_by_three']}")