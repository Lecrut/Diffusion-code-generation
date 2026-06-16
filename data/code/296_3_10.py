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
    scale_factor = target_first_term / start_a
    new_a = int(round(start_a * scale_factor))
    new_b = int(round(start_b * scale_factor))
    if new_a == 0 or new_b == 0:
        return None, None
    return new_a, new_b
if __name__ == '__main__':
    start_ratio = "2:3"
    target_value = 10
    try:
        new_a, new_b = adjust_ratio(start_ratio, target_value)
        print(f"Start Ratio: {start_ratio}")
        print(f"Target First Term: {target_value}")
        if new_a is not None:
            print(f"New Ratio (A:B): {new_a}:{new_b}")
    except ValueError as e:
        print(f"Error: {e}")
    start_ratio = "5:7"
    target_value = 20
    try:
        new_a, new_b = adjust_ratio(start_ratio, target_value)
        print(f"\nStart Ratio: {start_ratio}")
        print(f"Target First Term: {target_value}")
        if new_a is not None:
            print(f"New Ratio (A:B): {new_a}:{new_b}")
    except ValueError as e:
        print(f"Error: {e}")