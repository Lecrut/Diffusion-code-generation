def max_of_three(a: float, b: float, c: float) -> float:
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c

if __name__ == '__main__':
    print(max_of_three(1.5, 3.2, 2.8))