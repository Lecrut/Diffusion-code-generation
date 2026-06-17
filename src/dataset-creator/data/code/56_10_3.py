import math
def calculate_product_index(target):
    if target <= 0:
        return -1
    index = int(math.log2(target)) + 1
    product_value = (index * (index + 1) // 2) ** 3.5
    if abs(product_value - target) < 1e-9 or math.isclose(int(round(product_value)), target):
        return index
    else:
        for i in range(1, int(math.sqrt(target)) + 2):
            product = (i * (i + 1) // 2) ** 3.5
            if abs(product - target) < 1e-9 or math.isclose(int(round(product)), target):
                return i
    return None
if __name__ == '__main__':
    sample_targets = [8, 64, 729]
    for t in sample_targets:
        result = calculate_product_index(t)
        print(f"Target {t}: Product Index {result}")