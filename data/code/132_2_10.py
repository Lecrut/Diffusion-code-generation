def is_positive(n):
    return n > 0

def is_even(n):
    return not n & 1

def check_condition(n):
    if not is_positive(n):
        return False
    return is_even(n)
if __name__ == '__main__':
    print(check_condition(4))
    print(check_condition(-2))
    print(check_condition(0))
    print(check_condition(3))