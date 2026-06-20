def check_conditions(p: bool, q: bool) -> bool:
    condition_first = p and not q
    condition_second = not p and q
    return condition_first or condition_second

if __name__ == '__main__':
    sample_values = [(True, False), (False, True), (True, True), (False, False)]
    for val in sample_values:
        result = check_conditions(*val)
        print(result)