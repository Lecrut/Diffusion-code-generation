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
    new_b = int(target_first_term / ratio_value)
    new_a = int(start_a * (target_first_term / start_a))                                                                                                        
    new_second_term = int(target_first_term * start_b / start_a)
    return target_first_term, new_second_term
if __name__ == '__main__':
    start_ratio = "2:3"
    target = 10
    try:
        t1, t2 = adjust_ratio(start_ratio, target)
        print(f"Start Ratio: {start_ratio}")
        print(f"Target First Term: {target}")
        if t1 is not None:
            print(f"New First Term (T1): {t1}")
            print(f"New Second Term (T2): {t2}")
    except ValueError as e:
        print(f"Error: {e}")