def validate_positive_even_under_limit(x1, x2, x3):
    is_positive = x1 > 0 and x2 > 0 and x3 > 0
    is_even = x1 % 2 == 0 and x2 % 2 == 0 and x3 % 2 == 0
    is_under_limit = x1 < 100 and x2 < 100 and x3 < 100
    return is_positive and is_even and is_under_limit

if __name__ == '__main__':
    val_a = 12
    val_b = 45
    val_c = 88
    result = validate_positive_even_under_limit(val_a, val_b, val_c)
    print(result)