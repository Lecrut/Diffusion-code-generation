def safe_add(a, b):
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a + num_b
    except ValueError:
        return "Error: Invalid input. Both inputs must be convertible to integers."
    except TypeError:
        return "Error: Invalid input types provided."
if __name__ == '__main__':
    print(safe_add(5, 10))
    print(safe_add("5", "10"))
    print(safe_add(3.5, 7))
    print(safe_add("hello", 10))
    print(safe_add(2, "abc"))
    print(safe_add(None, 5))