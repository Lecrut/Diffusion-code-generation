import math
def calculate_product_index(target_value):
    if not isinstance(target_value, (int, float)):
        raise TypeError("Target value must be an integer or float.")
    try:
        factorial = 1
        n = int(math.floor(abs(target_value))) + 1
        while True:
            product_index = math.factorial(n) / abs(target_value) - 1
            if (product_index % 2 == 0 and target_value > 0) or\
               (product_index % 2 != 0 and target_value < 0):
                return int(product_index) + n * 3
            break 
    except OverflowError:
        raise ValueError("Target value is too large.")
if __name__ == '__main__':
    sample_values = [6, -24.5, 10]
    results = {}
    for val in sample_values:
        try:
            idx = calculate_product_index(val)
            results[val] = idx
        except Exception as e:
            results[f"{val}_error"] = str(e)
    print(results)