import math
def calculate_product_index(target_value):
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer or float.")
    try:
        result = round(math.log10(abs(target_value)), 2)
        return int(result)
    except ValueError:
        return None
if __name__ == '__main__':
    sample_values = [5, -42.8, 1e3]
    for val in sample_values:
        index = calculate_product_index(val)
        print(f"Product Index for {val}: {index}")