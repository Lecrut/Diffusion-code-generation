def compare_values(a, b):
    if type(a) is type(b):
        return a == b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a == b
    elif isinstance(a, str) and isinstance(b, str):
        return a == b
    else:
        try:
            if a == b:
                return True
            else:
                return False
        except (TypeError, ValueError):
            return False
if __name__ == '__main__':
    print(f"Int comparison (5, 5): {compare_values(5, 5)}")
    print(f"Int comparison (5, 6): {compare_values(5, 6)}")
    print(f"Float comparison (3.14, 3.14): {compare_values(3.14, 3.14)}")
    print(f"Float comparison (3.14, 3.15): {compare_values(3.14, 3.15)}")
    print(f"String comparison ('hello', 'hello'): {compare_values('hello', 'hello')}")
    print(f"String comparison ('hello', 'world'): {compare_values('hello', 'world')}")
    print(f"Mixed comparison (10, 10.0): {compare_values(10, 10.0)}")
    print(f"Mixed comparison ('a', 1): {compare_values('a', 1)}")
    print(f"List comparison ([1], [1]): {compare_values([1], [1])}")
    print(f"None comparison (None, None): {compare_values(None, None)}")
    print(f"None comparison (None, []): {compare_values(None, [])}")