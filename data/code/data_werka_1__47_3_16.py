def herons_formula(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Invalid triangle sides")
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

if __name__ == '__main__':
    try:
        print(herons_formula(6, 8, 10))
    except ValueError as e:
        print(e)