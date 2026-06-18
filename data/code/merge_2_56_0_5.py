import math
def calculate_product_index(target_value):
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer or float.")
    try:
        result = int(math.log10(abs(target_value))) + 1
        return result
    except ValueError:
        return None
if __name__ == '__main__':
    sample_values = [5, -3.2, 100, 999]
    for value in sample_values:
        index = calculate_product_index(value)
        print(f"Product Index for {value}: {index}")