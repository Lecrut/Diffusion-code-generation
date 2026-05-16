def compare_booleans(a: bool, b: bool) -> tuple[bool, str]:
    result = a == b
    operation = "=="
    return (result, operation)
if __name__ == '__main__':
    a_val = True
    b_val = False
    result, operation = compare_booleans(a_val, b_val)
    print(f"a: {a_val}, b: {b_val}")
    print(f"Result: {result}")
    print(f"Operation: {operation}")
    a_val = True
    b_val = True
    result, operation = compare_booleans(a_val, b_val)
    print(f"a: {a_val}, b: {b_val}")
    print(f"Result: {result}")
    print(f"Operation: {operation}")
    a_val = False
    b_val = False
    result, operation = compare_booleans(a_val, b_val)
    print(f"a: {a_val}, b: {b_val}")
    print(f"Result: {result}")
    print(f"Operation: {operation}")