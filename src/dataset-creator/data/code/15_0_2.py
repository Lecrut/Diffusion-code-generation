import sys
def safe_sort(numbers):
    try:
        numeric_list = [float(num) for num in numbers]
    except ValueError as e:
        print(f"Error: Non-numeric element found. Details: {e}")
        sys.exit(1)
    return sorted(numeric_list, reverse=False)
if __name__ == '__main__':
    sample_data = [3, -5, "2", 0.7, None, True]
    processed_input = []
    try:
        for item in sample_data:
            val = float(item)
            processed_input.append(val)
    except (ValueError, TypeError):
        print("Warning: Some elements could not be converted to numbers and were skipped.")
    result = safe_sort(processed_input) if len(sample_data) > 0 else []
    print(result)