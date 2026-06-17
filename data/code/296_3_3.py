def adjust_ratio(start_ratio_str, target_first_term):
    try:
        parts = [int(x.strip()) for x in start_ratio_str.split(':')]
        if len(parts) != 2 or parts[1] == 0:
            raise ValueError("Invalid ratio format or zero second term")
        start_a = parts[0]
        start_b = parts[1]
        if start_a == 0:
            return None, None
        scale_factor = target_first_term / start_a
        new_b_float = start_b * scale_factor
        new_b = (target_first_term * start_b) // start_a
        return target_first_term, new_b
    except ValueError:
        return None, None
    except Exception:
        return None, None
if __name__ == '__main__':
    start_ratio = "2:3"
    target = 10
    new_a, new_b = adjust_ratio(start_ratio, target)
    print(f"Start Ratio: {start_ratio}")
    print(f"Target First Term: {target}")
    if new_a is not None and new_b is not None:
        print(f"New First Term: {new_a}")
        print(f"New Second Term (Integer): {new_b}")
        print(f"Resulting Ratio: {new_a}:{new_b}")
    else:
        print("Calculation failed.")
    start_ratio = "5:2"
    target = 15
    new_a, new_b = adjust_ratio(start_ratio, target)
    print("\n--- Second Example ---")
    print(f"Start Ratio: {start_ratio}")
    print(f"Target First Term: {target}")
    if new_a is not None and new_b is not None:
        print(f"New First Term: {new_a}")
        print(f"New Second Term (Integer): {new_b}")
        print(f"Resulting Ratio: {new_a}:{new_b}")
    else:
        print("Calculation failed.")