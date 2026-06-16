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
    new_b_float = start_b * scale_factor
    new_a = target_first_term
    new_b = round(new_b_float) 
    change_a = new_a - start_a
    change_b = new_b - start_b
    return (new_a, new_b), (change_a, change_b)
if __name__ == '__main__':
    start_ratio = "2:3"
    target_first_term = 10
    try:
        result, changes = adjust_ratio(start_ratio, target_first_term)
        if result:
            new_a, new_b = result
            change_a, change_b = changes
            print(f"Start Ratio: {start_ratio}")
            print(f"Target First Term: {target_first_term}")
            print("-------------------------")
            print(f"New Ratio Achieved (A:B): {new_a}:{new_b}")
            print(f"Change in First Term (A): {change_a}")
            print(f"Change in Second Term (B): {change_b}")
    except ValueError as e:
        print(f"Error: {e}")