def adjust_ratio(start_ratio_str, target_first_term):
    try:
        start_a_str, start_b_str = start_ratio_str.split(':')
        start_a = int(start_a_str)
        start_b = int(start_b_str)
    except ValueError:
        return "Invalid start ratio format"
    if start_a == 0 or start_b == 0:
        return "Start terms cannot be zero"
    if target_first_term == 0:
        return "Target first term cannot be zero for division"
    scale_factor = target_first_term / start_a
    new_b_float = start_b * scale_factor
    new_b = int(round(target_first_term * (start_b / start_a)))
    return {
        "start_a": start_a,
        "start_b": start_b,
        "target_a": target_first_term,
        "new_b": new_b,
        "change_b": new_b - start_b
    }
if __name__ == '__main__':
    ratio1 = "2:3"
    target1 = 10
    result1 = adjust_ratio(ratio1, target1)
    print(f"Start Ratio: {ratio1}, Target First Term: {target1}")
    print(f"Result: {result1}")
    print("-" * 20)
    ratio2 = "5:7"
    target2 = 4
    result2 = adjust_ratio(ratio2, target2)
    print(f"Start Ratio: {ratio2}, Target First Term: {target2}")
    print(f"Result: {result2}")
    print("-" * 20)
    ratio3 = "10:10"
    target3 = 5
    result3 = adjust_ratio(ratio3, target3)
    print(f"Start Ratio: {ratio3}, Target First Term: {target3}")
    print(f"Result: {result3}")