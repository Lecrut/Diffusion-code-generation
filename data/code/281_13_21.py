def sum_six_integers(a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    total = 0
    numbers = [a, b, c, d, e, f]
    for num in numbers:
        total += num
    return total

if __name__ == '__main__':
    result1 = sum_six_integers(-20, -15, -10, 0, 5, 10)
    print(f"Sum of (-20, -15, -10, 0, 5, 10): {result1}")