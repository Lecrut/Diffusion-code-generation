import sys
def process_data(data_list):
    return [x for x in data_list if isinstance(x, (int, float)) and x > 0]
if __name__ == '__main__':
    sample_values = [10, -5, "error", None, 3.14, True, False, 20]
    try:
        result = process_data(sample_values)
        print(f"Filtered positive values: {result}")
    except Exception as e:
        if isinstance(e, TypeError):
            raise ValueError("Invalid input type detected in data list.") from None
        else:
            raise RuntimeError(f"Unexpected error occurred during processing: {e}")