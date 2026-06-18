import math
def calculate_product_index(target):
    if target <= 0:
        return -1
    product = 2
    index = 1
    while product < target:
        product *= 3
        index += 1
    if product == target:
        return index
    temp_target = target
    count_2 = 0
    while temp_target % 2 == 0:
        temp_target //= 2
        count_2 += 1
    remaining = math.log(temp_target, 3) if temp_target > 1 else 0
    total_factors = count_2 + int(remaining)
    return -1
if __name__ == '__main__':
    test_cases = [8, 9, 64, 72]
    for case in test_cases:
        print(f"Target {case}: Index {calculate_product_index(case)}")