def sum_seven_integers(a, b, c, d, e, f, g):
    if not all(isinstance(i, int) for i in [a, b, c, d, e, f, g]):
        raise ValueError("All inputs must be integers.")
    return a + b + c + d + e + f + g

if __name__ == '__main__':
    result1 = sum_seven_integers(1, 2, 3, 4, 5, 6, 7)
    print(f"Sum of (1, 2, 3, 4, 5, 6, 7): {result1}")
    result2 = sum_seven_integers(-10, -20, -30, 0, 5, 15, 25)
    print(f"Sum of (-10, -20, -30, 0, 5, 15, 25): {result2}")