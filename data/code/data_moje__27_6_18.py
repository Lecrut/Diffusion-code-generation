def check_triangle_validity(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a + b > c and a + c > b and b + c > a:
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    result = check_triangle_validity(3, 4, 5)
    print(result)
    result2 = check_triangle_validity(1, 2, 3)
    print(result2)
    result3 = check_triangle_validity(5, 5, 5)
    print(result3)