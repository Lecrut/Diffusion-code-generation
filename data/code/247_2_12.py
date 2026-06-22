def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Error: Both inputs must be integers or floats")
    return a + b

if __name__ == '__main__':
    print(f"10 + 5 = {add(10, 5)}")
    print(f"3.14 + 2 = {add(3.14, 2)}")
    print(f"'a' + 'b' = {add('a', 'b')}")
    print(f"5 + 'text' = {add(5, 'text')}")