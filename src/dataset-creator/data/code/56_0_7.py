import math
def calculate_product_index(target_value: float) -> int:
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be numeric.")
    if target_value <= 0:
        return -1
    log_target = math.log(target_value)
    product_index = int(round(log_target)) + 1
    return product_index
if __name__ == '__main__':
    target_values = [2.5, 100, 73948]
    for val in target_values:
        index = calculate_product_index(val)
        print(f"Target Value: {val}, Product Index: {index}")