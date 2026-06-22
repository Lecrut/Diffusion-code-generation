def check_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    result = check_triangle(side1, side2, side3)
    print(result)