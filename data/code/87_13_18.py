def check_conditions(x: bool, y: bool) -> bool:
    condition1 = x and not y
    condition2 = not x and y
    return condition1 or condition2

if __name__ == '__main__':
    sample_values = [(True, False), (False, True), (True, True), (False, False)]
    for val in sample_values:
        result = check_conditions(*val)
        print(result)