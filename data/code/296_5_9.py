def calculate_scaled_ratio(ratio, target):
    if target == 0:
        return 0
    new_ratio = (ratio * target) / target
    return new_ratio
if __name__ == '__main__':
    ratio1 = 2
    target1 = 10
    result1 = calculate_scaled_ratio(ratio1, target1)
    print(f"Ratio: {ratio1}, Target: {target1}, Result: {result1}")
    ratio2 = 3
    target2 = 15
    result2 = calculate_scaled_ratio(ratio2, target2)
    print(f"Ratio: {ratio2}, Target: {target2}, Result: {result2}")
    ratio3 = 4
    target3 = 0
    result3 = calculate_scaled_ratio(ratio3, target3)
    print(f"Ratio: {ratio3}, Target: {target3}, Result: {result3}")
    ratio4 = 5
    target4 = 25
    result4 = calculate_scaled_ratio(ratio4, target4)
    print(f"Ratio: {ratio4}, Target: {target4}, Result: {result4}")