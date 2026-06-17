def calculate_ratio_change(start_ratio_str, target_first_term):
    try:
        start_a, start_b = map(int, start_ratio_str.split(':'))
    except ValueError:
        return "Invalid ratio format"
    if start_a == 0 or start_b == 0:
        return "Start terms cannot be zero"
    if target_first_term == 0:
        return "Target first term cannot be zero"
    new_b_float = (target_first_term * start_b) / start_a
    if new_b_float == int(new_b_float):
        new_b = int(new_b_float)
        change_a = target_first_term - start_a
        change_b = new_b - start_b
        return {
            "start_a": start_a,
            "start_b": start_b,
            "target_a": target_first_term,
            "new_b": new_b,
            "change_a": change_a,
            "change_b": change_b
        }
    else:
        return "Ratio calculation resulted in non-integer terms"
if __name__ == '__main__':
    start_ratio = "2:3"
    target = 10
    result = calculate_ratio_change(start_ratio, target)
    print(result)
    start_ratio = "4:5"
    target = 20
    result = calculate_ratio_change(start_ratio, target)
    print(result)
    start_ratio = "1:1"
    target = 5
    result = calculate_ratio_change(start_ratio, target)
    print(result)