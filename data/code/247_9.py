def safe_add(a, b):
    try:
        int_a = int(a)
        int_b = int(b)
        return int_a + int_b
    except ValueError:
        raise ValueError("Inputs must be convertible to integers")
if __name__ == '__main__':
    print(safe_add(10, 5))
    try:
        safe_add("hello", 5)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    try:
        safe_add(3.5, "2")
    except ValueError as e:
        print(f"Caught expected error: {e}")