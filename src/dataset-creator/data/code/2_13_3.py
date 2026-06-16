import sys
def process_data(data_list):
    return [x for x in data_list if isinstance(x, (int, float)) and x > 0]
if __name__ == '__main__':
    sample_values = [10, -5, "error", None, 3.14, True, False, 20]
    try:
        result = process_data(sample_values)
        print(f"Valid positive values found: {result}")
    except Exception as e:
        sys.exit(1)