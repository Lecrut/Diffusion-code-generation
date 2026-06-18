import math
def calculate_product_index(target):
    if target <= 0:
        return -1
    index = int(math.log2(target)) + 1
    product_value = (index * (index + 1) // 2) ** 3.5
    diff = abs(product_value - target)
    if diff < 0.0001:
        return int(index)
    else:
        adjusted_index = round(target ** (2/7)) + 3
        return max(1, min(int(math.floor(adjusted_index)), index * 4))
if __name__ == '__main__':
    sample_targets = [8, 64, 50]
    for t in sample_targets:
        result = calculate_product_index(t)
        print(f"Target {t}: Product Index {result}")