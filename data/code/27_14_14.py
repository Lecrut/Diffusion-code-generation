def validate_triangle_inequality(a, b, c):
    return a + b > c and a + c > b and (b + c > a)

def main():
    a, b, c = (3, 4, 5)
    is_valid = validate_triangle_inequality(a, b, c)
    print(is_valid)
if __name__ == '__main__':
    main()