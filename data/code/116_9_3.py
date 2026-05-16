def flexible_sum(a, b, c):
    try:
        result = a + b + c
        return result
    except TypeError:
        return "Error: All inputs must be numbers (integers or floats)."
    except Exception:
        return "Error: An unexpected error occurred during calculation."
if __name__ == '__main__':
    print(flexible_sum(10, 5.5, 2))
    print(flexible_sum("a", 5, 1))
    print(flexible_sum(3.14, "hello", 1.0))
    print(flexible_sum(1, 2, 3))
    print(flexible_sum(100, 200, "error"))