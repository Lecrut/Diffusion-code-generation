import sys
def validate_numeric_string(s: str) -> bool:
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False
def secure_sort_handler(input_list: list[str]) -> list[float]:
    valid_numbers = []
    for item in input_list:
        if validate_numeric_string(item.strip()):
            num_value = float(item.strip())
            valid_numbers.append(num_value)
    try:
        sorted_values = sorted(valid_numbers, reverse=True)
        return [str(x) for x in sorted_values]
    except Exception as e:
        print(f"Sorting error occurred: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_inputs = ["abc", "  -3.5 ", "", "+7", "not a number", "0"]
    result_list = secure_sort_handler(sample_inputs)
    print("Sorted numeric values:", ', '.join(result_list))