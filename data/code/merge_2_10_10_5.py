def extract_numeric_value(item):
    try:
        return float(str(item).strip())
    except ValueError as e:
        raise TypeError(f"Cannot convert non-numeric element '{item}' to a number.") from e
if __name__ == '__main__':
    mixed_data = ["10", "apple", 3.5, "-2", None, "42"]
    try:
        sorted_items = sorted(mixed_data, key=extract_numeric_value)
        print(sorted_items)
    except TypeError as e:
        print(f"Error processing data: {e}")