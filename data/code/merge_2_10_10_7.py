def extract_number(s):
    try:
        return float(s)
    except ValueError as e:
        raise TypeError(f"Cannot convert '{s}' to a number") from e
if __name__ == '__main__':
    mixed_data = ["42", "apple", "-3.5", "banana10", "", "7"]
    try:
        sorted_items = list(filter(lambda x: extract_number(x) is not None, mixed_data))
        numeric_values = [extract_number(item) for item in sorted_items]
        final_sorted_list = []
        for i, val in enumerate(numeric_values):
            original_item = sorted_items[i]
            try:
                float(original_item)
                final_sorted_list.append((val, original_item))
            except ValueError:
                raise TypeError(f"Non-numeric element found that could not be processed: '{original_item}'")
        final_sorted_list.sort(key=lambda x: -x[0])
        print("Sorted list:", [(num, str(item)) for num, item in final_sorted_list])
    except TypeError as te:
        print(f"Error occurred during processing: {te}")