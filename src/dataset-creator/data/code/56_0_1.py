import math
def calculate_product_index(target_value: float) -> int:
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be numeric.")
    if target_value <= 0:
        return -1
    log_target = math.log2(target_value)
    max_factorial_index = int(math.floor(log_target)) + 1
    current_product = 1.0
    for i in range(1, max_factorial_index):
        if target_value <= (i ** i * (i+1)):
            return i
    return -2
if __name__ == '__main__':
    sample_values = [64, 128, 0.5]
    for val in sample_values:
        index_result = calculate_product_index(val)
        print(f"Target Value: {val}, Product Index: {index_result}")