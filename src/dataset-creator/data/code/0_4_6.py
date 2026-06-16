def check_equality(a: any, b: any) -> bool:
    if type(a) != type(b):
        return False
    try:
        a_id = id(a)
        b_id = id(b)
        if isinstance(a, (int, float)):
            return a == b
        elif isinstance(a, str):
            return a is b or a == b
        else:
            return a is b
    except Exception as e:
        print(f"Error during comparison: {e}")
        return False
if __name__ == '__main__':
    x = 5
    y = 5.0
    z = "hello"
    result1 = check_equality(x, y)
    result2 = check_equality(z, z)
    result3 = check_equality([1, 2], [1, 2])
    print(f"x == y: {result1}")
    print(f"z is z: {result2}")
    print(f"[1,2] == [1,2]: {result3}")