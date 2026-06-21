def check_even(n):
    if isinstance(n, bool):
        return "ERROR: Non-integer input"
    if not isinstance(n, int):
        return "ERROR: Non-integer input"
    return n % 2 == 0

if __name__ == '__main__':
    print(check_even(4))
    print(check_even(3))
    print(check_even("string"))
    print(check_even(3.14))