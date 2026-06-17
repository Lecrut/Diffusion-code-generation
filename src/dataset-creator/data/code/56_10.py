import math
def calculate_product_index(target):
    if target <= 0:
        return -1
    index = int(math.log2(target)) + 1
    product_value = (index ** 3) * index
    while product_value < target and index > 1:
        index += 1
        product_value = (index ** 3) * index
    if product_value == target or abs(product_value - target) <= 0.5:
        return int(index)
    return -1
if __name__ == '__main__':
    sample_targets = [8, 27, 64, 125]
    for t in sample_targets:
        result = calculate_product_index(t)
        print(f"Target {t}: Index {result}")