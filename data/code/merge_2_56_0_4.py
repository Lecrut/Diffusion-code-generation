import math
def calculate_product_index(target_value):
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer or float.")
    try:
        result = int(math.log10(abs(target_value))) + 1
        return result
    except ValueError:
        raise ValueError("Input cannot be zero or negative for logarithmic calculation.")
if __name__ == '__main__':
    sample_values = [5, -3.2, 1e6]
    for val in sample_values:
        try:
            index = calculate_product_index(val)
            print(f"Product Index for {val}: {index}")
        except Exception as e:
            print(f"Error processing {val}: {str(e)}")