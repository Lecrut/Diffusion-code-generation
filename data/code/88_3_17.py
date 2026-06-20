def check_both_conditions(a: bool, b: bool) -> bool:
    result = a and b
    return result

if __name__ == '__main__':
    condition_x = True
    condition_y = False
    outcome = check_both_conditions(condition_x, condition_y)
    print("Both conditions met:", outcome)