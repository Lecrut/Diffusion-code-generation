def flexible_sum(a, b, c):
    if not all(isinstance(x, (int, float, str)) for x in [a, b, c]):
        raise TypeError("All arguments must be integers, floats, or strings.")
    try:
        sum_val = a + b + c
        return sum_val
    except TypeError:
        raise TypeError("One or more arguments are not compatible for addition.")
if __name__ == '__main__':
    print(flexible_sum(1, 2, 3))
    print(flexible_sum(1.5, 2.5, 3.0))
    print(flexible_sum("a", "b", "c"))
    try:
        flexible_sum(1, 2, "a")
    except TypeError as e:
        print(f"Error: {e}")
    try:
        flexible_sum(1, "a", 3)
    except TypeError as e:
        print(f"Error: {e}")
    try:
        flexible_sum(1, 2, None)
    except TypeError as e:
        print(f"Error: {e}")