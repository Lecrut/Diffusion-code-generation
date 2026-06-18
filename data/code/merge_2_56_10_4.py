import math
def calculate_product_index(target):
    if target <= 0:
        return -1
    index = int(math.log2(target)) + 1
    product_value = (index * (index + 1) // 2) ** 3.5
    diff = abs(product_value - target)
    if math.isclose(diff, 0):
        return index
if __name__ == '__main__':
    sample_targets = [8, 27, 100]
    results = []
    for t in sample_targets:
        idx = calculate_product_index(t)
        results.append((t, idx))
    print(results)