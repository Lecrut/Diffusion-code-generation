def calculate_scaled_ratio(original_ratio, target_value):
    if original_ratio == 0:
        return 0
    new_ratio = (target_value / original_ratio) * original_ratio
    return new_ratio
if __name__ == '__main__':
    ratio1 = 2
    target1 = 10
    result1 = calculate_scaled_ratio(ratio1, target1)
    print(f"Original Ratio: {ratio1}, Target Value: {target1}, New Ratio: {result1}")
    ratio2 = 5
    target2 = 25
    result2 = calculate_scaled_ratio(ratio2, target2)
    print(f"Original Ratio: {ratio2}, Target Value: {target2}, New Ratio: {result2}")
    ratio3 = 10
    target3 = 4
    result3 = calculate_scaled_ratio(ratio3, target3)
    print(f"Original Ratio: {ratio3}, Target Value: {target3}, New Ratio: {result3}")
    ratio4 = 0
    target4 = 10
    result4 = calculate_scaled_ratio(ratio4, target4)
    print(f"Original Ratio: {ratio4}, Target Value: {target4}, New Ratio: {result4}")