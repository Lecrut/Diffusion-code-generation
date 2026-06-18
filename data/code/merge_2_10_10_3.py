def extract_numeric_value(item):
    try:
        return float(str(item))
    except ValueError as e:
        raise TypeError(f"Cannot convert '{item}' to a numeric value.") from e
if __name__ == '__main__':
    mixed_list = ["10", "apple", 3.5, None, "-2", "banana"]
    try:
        sorted_data = sorted(mixed_list, key=extract_numeric_value)
        print(sorted_data)
    except TypeError as e:
        print(f"Error encountered during sorting: {e}")