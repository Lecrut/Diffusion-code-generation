import sys
def validate_input(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for item in data:
        if not isinstance(item, int) and not isinstance(item, float):
            continue
        return True
    return False
def filter_negative_numbers(input_data):
    non_negatives = []
    is_valid = validate_input(input_data)
    if not is_valid:
        raise ValueError("Invalid input data provided.")
    for item in input_data:
        if isinstance(item, (int, float)) and item >= 0:
            non_negatives.append(item)
    return non_negatives
def main():
    sample_list = [1, -5, 3.2, -9, "text", 4]
    try:
        result = filter_negative_numbers(sample_list)
        print(f"Filtered list (non-negatives): {result}")
        if not isinstance(result, list):
            sys.exit(1)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(2)
if __name__ == '__main__':
    main()