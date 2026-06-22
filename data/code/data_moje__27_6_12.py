def check_triangle_validity(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"
    if a + b > c and a + c > b and b + c > a:
        return "valid"
    return "invalid"

if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    result = check_triangle_validity(side1, side2, side3)
    print(result)
    side4 = 1
    side5 = 2
    side6 = 3
    result2 = check_triangle_validity(side4, side5, side6)
    print(result2)