import sys
def safe_sort(numbers):
    if not numbers:
        return []
    try:
        numeric_list = [float(x) for x in numbers]
    except (ValueError, TypeError):
        raise ValueError("List contains non-numeric elements.") from None
    sorted_numbers = sorted(numeric_list)
    return [int(x) if x == int(x) else float(x) for x in sorted_numbers]
if __name__ == '__main__':
    sample_data = [-5, "10", 3.7, None, -2, True, 4, False, "", 8.9]
    try:
        result = safe_sort(sample_data)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)