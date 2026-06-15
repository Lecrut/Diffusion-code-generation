def safe_add(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        return num_a + num_b
    except ValueError:
        return "Error: Invalid input. Both inputs must be numeric."
if __name__ == '__main__':
    print(safe_add(10, 5))
    print(safe_add("12.5", 3.5))
    print(safe_add("hello", 5))
    print(safe_add(20, "invalid"))
    print(safe_add("", 10))