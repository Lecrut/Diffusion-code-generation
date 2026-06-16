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
    if new_a == 0:
        return None, None
    new_b_calculated = (new_b / new_a) * start_b
    new_b_final = (target_first_term * start_b) // start_a
    return target_first_term, new_b_final
if __name__ == '__main__':
    start_ratio = "2:3"
    target = 10
    try:
        new_first, new_second = adjust_ratio(start_ratio, target)
        print(f"Start Ratio: {start_ratio}")
        print(f"Target First Term: {target}")
        if new_first is not None:
            print(f"New Ratio (First Term): {new_first}")
            print(f"New Ratio (Second Term): {new_second}")
            print(f"Resulting Ratio: {new_first}:{new_second}")
        else:
            print("Could not calculate a valid integer ratio.")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    start_ratio = "5:7"
    target = 15
    try:
        new_first, new_second = adjust_ratio(start_ratio, target)
        print(f"Start Ratio: {start_ratio}")
        print(f"Target First Term: {target}")
        if new_first is not None:
            print(f"New Ratio (First Term): {new_first}")
            print(f"New Ratio (Second Term): {new_second}")
            print(f"Resulting Ratio: {new_first}:{new_second}")
        else:
            print("Could not calculate a valid integer ratio.")
    except ValueError as e:
        print(f"Error: {e}")