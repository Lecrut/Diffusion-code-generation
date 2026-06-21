def check_even(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return "ERROR: Input must be an integer."
    if n % 2 == 0:
        return True
    return False

if __name__ == '__main__':
    print(check_even(4))
    print(check_even(3))
    print(check_even("string"))
    print(check_even(3.5))