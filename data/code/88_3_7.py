def check_conditions_met(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    condition_x = False
    condition_y = True
    result = check_conditions_met(condition_x, condition_y)
    print("Both conditions met:", result)