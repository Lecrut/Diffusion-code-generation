def validate_data(data):
    if not data:
        raise ValueError("The input list is empty.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("The list contains non-numeric types.")

def calculate_range(data):
    validate_data(data)
    return max(data) - min(data)

if __name__ == '__main__':
    sample_list = [10, 5.5, 20, 3.14]
    try:
        result = calculate_range(sample_list)
        print(f"Range of {sample_list}: {result}")
    except ValueError as e:
        print(e)

    sample_list_empty = []
    try:
        result = calculate_range(sample_list_empty)
        print(f"Range of {sample_list_empty}: {result}")
    except ValueError as e:
        print(e)

    sample_list_non_numeric = [10, 'five', 20]
    try:
        result = calculate_range(sample_list_non_numeric)
        print(f"Range of {sample_list_non_numeric}: {result}")
    except ValueError as e:
        print(e)