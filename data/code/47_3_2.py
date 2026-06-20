def heron_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

if __name__ == '__main__':
    print(heron_area(3, 4, 5))