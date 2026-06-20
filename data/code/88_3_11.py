def check_conditions_met(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    condition_a = True
    condition_b = False
    print("Result:", check_conditions_met(condition_a, condition_b))