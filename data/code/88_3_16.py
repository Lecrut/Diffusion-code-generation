def check_conditions_met(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    result = check_conditions_met(True, False)
    print(result)