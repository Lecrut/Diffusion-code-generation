def validate_input(a: int, b: int, c: int) -> bool:
    threshold = 100
    lower_bound = 0
    even_mask = 1
    is_valid = lambda val: val > lower_bound and val < threshold and (val & even_mask) == 0
    return is_valid(a) and is_valid(b) and is_valid(c)

if __name__ == '__main__':
    print(validate_input(2, 4, 6))
    print(validate_input(2, 4, 100))
    print(validate_input(2, 3, 6))
    print(validate_input(-2, 4, 6))
    print(validate_input(0, 4, 6))