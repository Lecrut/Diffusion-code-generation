def flexible_sum(a, b, c):
    try:
        result = a + b + c
        return result
    except TypeError:
        return "Error: All inputs must be numeric (int or float) to calculate the sum."
    except Exception:
        return "Error: An unexpected error occurred during summation."
if __name__ == '__main__':
    print(flexible_sum(10, 5.5, 2))
    print(flexible_sum("a", 5, 3))
    print(flexible_sum(1, 2, "three"))
    print(flexible_sum(10, 20, 30))
    print(flexible_sum(1.5, 2.5, 3.0))
    print(flexible_sum("hello", "world", "test"))