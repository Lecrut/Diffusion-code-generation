def add(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both arguments must be integers or floats")
    return a + b

if __name__ == '__main__':
    print(f"10 + 5 = {add(10, 5)}")
    print(f"3.14 + 2 = {add(3.14, 2)}")
    try:
        print(f"'a' + 'b' = {add('a', 'b')}")
    except ValueError as e:
        print(e)
    try:
        print(f"5 + 'text' = {add(5, 'text')}")
    except ValueError as e:
        print(e)