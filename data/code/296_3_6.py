def adjust_ratio(start_ratio_str, target_first_term):
    parts = start_ratio_str.split(':')
    if len(parts) != 2:
        raise ValueError("Invalid ratio format. Use 'a:b'")
    try:
        start_a = int(parts[0])
        start_b = int(parts[1])
    except ValueError:
        raise ValueError("Ratio parts must be integers")
    if start_a == 0 or start_b == 0:
        raise ValueError("Ratio components cannot be zero")
    if target_first_term == 0:
        return None, None
    ratio_value = start_a / start_b
    target_b = (target_first_term * start_b) / start_a
    numerator = target_first_term * start_b
    denominator = start_a
    if numerator % denominator != 0:
        return None, None
    new_b = numerator // denominator
    change_a = target_first_term - start_a
    change_b = new_b - start_b
    return change_a, change_b
if __name__ == '__main__':
    start_ratio = "2:3"
    target = 10
    try:
        change_a, change_b = adjust_ratio(start_ratio, target)
        if change_a is not None and change_b is not None:
            print(f"Start Ratio: {start_ratio}")
            print(f"Target First Term: {target}")
            print(f"Change in first term (a): {change_a}")
            print(f"Change in second term (b): {change_b}")
            new_a = 2 + change_a
            new_b = 3 + change_b
            print(f"New Ratio: {new_a}:{new_b}")
            print(f"New Ratio Value: {new_a/new_b}")
        else:
            print("Could not calculate the required changes.")
    except ValueError as e:
        print(f"Error: {e}")