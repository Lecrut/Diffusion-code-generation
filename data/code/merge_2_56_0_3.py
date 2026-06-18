import math
def calculate_product_index(target_value):
    if target_value <= 0:
        raise ValueError("Target value must be positive.")
    factorial = 1
    index = 1
    while True:
        next_factorial = factorial * (index + 1)
        if next_factorial == target_value:
            return index
        elif next_factorial < target_value and math.log(target_value, index + 2) > math.log(factorial, index):
            break
        else:
            raise ValueError(f"Target value {target_value} is not a factorial number.")
    if __name__ == '__main__':
        sample_values = [6, 120, 720]
        for val in sample_values:
            try:
                result_index = calculate_product_index(val)
                print(f"Product index for {val} is {result_index}")
            except ValueError as e:
                print(f"Error calculating product index for {val}: {e}")