ZERO = 0

def check_triangle(a, b, c):
    positive = a > ZERO and b > ZERO and c > ZERO
    if not positive:
        return False
    valid_sum = (a + b > c) and (a + c > b) and (b + c > a)
    return valid_sum

if __name__ == '__main__':
    print(check_triangle(3, 4, 5))
    print(check_triangle(1, 1, 1))
    print(check_triangle(0, 5, 5))
    print(check_triangle(-1, 2, 3))
    print(check_triangle(1, 2, 3))
    print(check_triangle(10, 10, 10))