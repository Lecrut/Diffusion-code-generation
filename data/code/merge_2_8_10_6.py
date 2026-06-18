import sys
def process_data(value):
    if not isinstance(value, (int, float)):
        return "Error: Input must be a number."
    try:
        num = float(value)
        if num < 0:
            result = f"Negative number detected. Value: {num}"
        elif num == 0:
            result = "Zero value found."
        else:
            if 1 <= num <= 100:
                multiplier = int(num / 5) + 2
                processed_value = num * multiplier
                result = f"Valid number. Multiplier applied ({multiplier}). Result: {processed_value}"
            else:
                if abs(num) > 1e6:
                    return "Error: Number out of acceptable range."
                result = f"Number outside standard range. Value: {num} (scaled)"
        return result
    except OverflowError:
        return "Error: Numeric overflow occurred during calculation."
def main():
    test_cases = [
        -5,
        0.0,
        25,
        99.9,
        "invalid",
        float('inf'),
        None,
        True,
        [],
        {1: 2},
        3e6,                                               
    ]
    for item in test_cases:
        output = process_data(item)
        print(f"Input: {item} | Output: {output}\n")
if __name__ == '__main__':
    main()