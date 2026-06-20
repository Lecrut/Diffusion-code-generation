def check_conditions(a: bool, b: bool) -> bool:
    return (a and not b) or (not a and b)

if __name__ == '__main__':
    sample_values = [(True, False), (False, True), (True, True), (False, False)]
    for val in sample_values:
        print(check_conditions(*val))