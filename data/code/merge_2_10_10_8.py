def extract_numeric_value(item):
    try:
        return float(str(item))
    except ValueError:
        raise TypeError(f"Cannot convert non-numeric element '{item}' to a number for sorting.")
if __name__ == '__main__':
    mixed_data = ["10", "banana", 3.5, None, "-2", "apple"]
    try:
        sorted_items = sorted(mixed_data, key=extract_numeric_value)
        print("Sorted list:", [str(x) for x in sorted_items])
    except TypeError as e:
        print(f"Error encountered during sorting: {e}")