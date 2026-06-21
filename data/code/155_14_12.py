def validate_list_elements(data_list):
    if not all(isinstance(item, float) for item in data_list):
        raise ValueError("All elements must be floats")

def calculate_list_sum(data_list):
    total = 0.0
    for item in data_list:
        total += item
    return total

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    validate_list_elements(sample_values)
    result = calculate_list_sum(sample_values)
    print(result)