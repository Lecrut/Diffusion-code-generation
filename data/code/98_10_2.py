def check_all_conditions(a: bool, b: bool, c: bool) -> bool:
    return a and b and c
if __name__ == '__main__':
    condition_a = True
    condition_b = False
    condition_c = True
    result = check_all_conditions(condition_a, condition_b, condition_c)
    print(f"Condition A: {condition_a}")
    print(f"Condition B: {condition_b}")
    print(f"Condition C: {condition_c}")
    print(f"Result of all conditions being met: {result}")