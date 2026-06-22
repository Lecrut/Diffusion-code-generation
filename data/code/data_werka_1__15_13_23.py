def validate_exact_match(arg1, arg2):
    return arg1 is arg2
if __name__ == '__main__':
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print(validate_exact_match(a, b))
    print(validate_exact_match(a, c))