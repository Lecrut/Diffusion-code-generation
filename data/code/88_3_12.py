def check_conditions_met(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    condition_x = True
    condition_y = False
    result = check_conditions_met(condition_x, condition_y)
    print("Result:", "Both are true" if result else "At least one is false")