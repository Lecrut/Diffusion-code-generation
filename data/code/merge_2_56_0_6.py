import math
def calculate_product_index(target_value):
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer or float.")
    try:
        result = int(math.log10(abs(target_value))) + 1
        return result
    except ValueError:
        raise ValueError("Product index cannot be calculated for zero values.")
if __name__ == '__main__':
    sample_values = [5, -3.2, 10**7]
    for val in sample_values:
        try:
            idx = calculate_product_index(val)
            print(f"Product index for {val}: {idx}")
        except Exception as e:
            print(f"Error calculating product index for {val}: {e}")