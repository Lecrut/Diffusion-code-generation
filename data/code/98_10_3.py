def check_all_conditions(a: bool, b: bool, c: bool) -> bool:
    return a and b and c
if __name__ == '__main__':
    value_a = True
    value_b = True
    value_c = False
    result = check_all_conditions(value_a, value_b, value_c)
    print(f"Value A: {value_a}")
    print(f"Value B: {value_b}")
    print(f"Value C: {value_c}")
    print(f"Result of check_all_conditions: {result}")