def compare_values(a, b):
    if type(a) is type(b):
        return a == b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a == b
    elif isinstance(a, str) and isinstance(b, str):
        return a == b
    else:
        try:
            return a == b
        except Exception:
            return False
if __name__ == '__main__':
    print(f"Integers: {compare_values(10, 10)}")
    print(f"Integers unequal: {compare_values(10, 20)}")
    print(f"Floats equal: {compare_values(3.14, 3.14)}")
    print(f"Floats unequal: {compare_values(3.14, 3.15)}")
    print(f"Strings equal: {compare_values('hello', 'hello')}")
    print(f"Strings unequal: {compare_values('hello', 'world')}")
    print(f"Mixed types (int vs str): {compare_values(10, '10')}")
    print(f"Mixed types (float vs int): {compare_values(5.0, 5)}")
    print(f"Different types: {compare_values([1], [1])}")
    print(f"Different types: {compare_values(None, None)}")