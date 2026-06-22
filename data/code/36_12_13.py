def trapezoid_area(b1, b2, height):
    if b1 < 0 or b2 < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return (b1 + b2) * height / 2

if __name__ == '__main__':
    b1 = 10
    b2 = 8
    height = 5
    print(trapezoid_area(b1, b2, height))