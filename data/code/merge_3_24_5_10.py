import sys

def process_numbers(numbers):
    """Iterate through a list of integers and print whether each is negative."""
    for num in numbers:
        if isinstance(num, int) and not isinstance(num, bool):
            status = "negative" if num < 0 else "non-negative"
            print(f"{num} is {status}")
        else:
            # Handle cases where input might be parsed incorrectly or non-integers exist in list
            pass

def safe_int_parser(value_str):
    """Attempt to convert a string to an integer. Returns None on failure."""
    try:
        return int(float(value_str)) if '.' in value_str else int(value_str)
    except (ValueError, TypeError):
        print(f"Warning: '{value_str}' is not a valid integer input.")
        return None

def main():
    """Main function to read integers from pre-defined sample values."""
    # Hard-coded sample values as per requirements (no user input or args)
    sample_values = [10, -5.7, "abc", 42, "-3"]

    processed_list = []
    
    for item in sample_values:
        if isinstance(item, int):
            processed_list.append(item)
        elif isinstance(item, str):
            parsed_value = safe_int_parser(item.strip())
            if parsed_value is not None:
                processed_list.append(parsed_value)

    process_numbers(processed_list)

if __name__ == '__main__':
    main()