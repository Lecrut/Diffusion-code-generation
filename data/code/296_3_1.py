def adjust_ratio(start_ratio_str, target_first_term):
    parts = start_ratio_str.split(':')
    if len(parts) != 2:
        raise ValueError("Invalid ratio format. Use A:B")
    try:
        start_a = int(parts[0])
        start_b = int(parts[1])
    except ValueError:
        raise ValueError("Ratio parts must be integers.")
    if start_a == 0 or start_b == 0:
        raise ValueError("Ratio terms cannot be zero.")
    if target_first_term == 0:
        return None, None
    ratio_value = start_a / start_b
    target_b = int(round(target_first_term * (start_b / start_a)))
    numerator = target_first_term * start_b
    denominator = start_a
    if numerator % denominator != 0:
        new_b = numerator / denominator
    else:
        new_b = numerator // denominator
    return target_first_term, new_b
if __name__ == '__main__':
    start_ratio = "2:3"
    target = 10
    try:
        new_a, new_b = adjust_ratio(start_ratio, target)
        print(f"Start Ratio: {start_ratio}")
        print(f"Target First Term: {target}")
        if new_a is not None:
            print(f"New Ratio (A:B): {new_a}:{new_b}")
        else:
            print("Calculation resulted in an undefined state.")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    start_ratio = "1:4"
    target = 5
    try:
        new_a, new_b = adjust_ratio(start_ratio, target)
        print(f"Start Ratio: {start_ratio}")
        print(f"Target First Term: {target}")
        if new_a is not None:
            print(f"New Ratio (A:B): {new_a}:{new_b}")
        else:
            print("Calculation resulted in an undefined state.")
    except ValueError as e:
        print(f"Error: {e}")