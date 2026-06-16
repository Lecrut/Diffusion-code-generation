import sys
def safe_sort(numbers):
    if not numbers:
        return []
    try:
        numeric_list = [float(x) for x in numbers]
        sorted_numbers = sorted(numeric_list)
        result = []
        for i, val in enumerate(sorted_numbers):
            if isinstance(numbers[i], int):
                result.append(int(val))
            else:
                result.append(float(val))
        return result
    except (ValueError, TypeError) as e:
        print(f"Error during sorting: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_data = [3.5, 2, '4', -1, None, True]
    try:
        mixed_input = [30, 25.9, '10', -5, True] 
        sorted_result = safe_sort(mixed_input)
        print("Sorted list:", sorted_result)
    except Exception as e:
        print(f"Input validation failed for mixed types or non-numeric values: {e}", file=sys.stderr)