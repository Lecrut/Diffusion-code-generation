import sys
def find_largest_element(elements):
    if not elements:
        raise ValueError("Input list cannot be empty.")
    max_value = None
    for item in elements:
        try:
            num = float(item)
        except (ValueError, TypeError):
            return f"Error: Non-numeric element '{item}' found."
        if max_value is None or num > max_value:
            max_value = num
    return int(max_value)
def main():
    sample_list = ["10", "2.5", "-3", 4, "abc"]
    result = find_largest_element(sample_list)
    print(result)
if __name__ == '__main__':
    main()