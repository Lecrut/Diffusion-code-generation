def safe_add(a, b):
    try:
        int_a = int(a)
        int_b = int(b)
        return int_a + int_b
    except ValueError:
        raise ValueError("One or both inputs could not be converted to an integer")
if __name__ == '__main__':
    print(safe_add(5, 3))
    try:
        safe_add("hello", 3)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    try:
        safe_add(10.5, "2")
    except ValueError as e:
        print(f"Caught expected error: {e}")