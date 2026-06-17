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
    new_a = target_first_term
    new_b = int(round(start_b * scale_factor))
    return new_a, new_b
if __name__ == '__main__':
    ratio1 = "2:3"
    target1 = 10
    print(f"Start Ratio: {ratio1}, Target First Term: {target1}")
    try:
        new_a1, new_b1 = adjust_ratio(ratio1, target1)
        if new_a1 is not None:
            print(f"New Ratio (A:B): {new_a1}:{new_b1}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    ratio2 = "5:7"
    target2 = 25
    print(f"Start Ratio: {ratio2}, Target First Term: {target2}")
    try:
        new_a2, new_b2 = adjust_ratio(ratio2, target2)
        if new_a2 is not None:
            print(f"New Ratio (A:B): {new_a2}:{new_b2}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    ratio3 = "1:4"
    target3 = 5
    print(f"Start Ratio: {ratio3}, Target First Term: {target3}")
    try:
        new_a3, new_b3 = adjust_ratio(ratio3, target3)
        if new_a3 is not None:
            print(f"New Ratio (A:B): {new_a3}:{new_b3}")
    except ValueError as e:
        print(f"Error: {e}")