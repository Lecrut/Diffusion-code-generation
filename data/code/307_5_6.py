def repeat_string(substring, n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("N must be a positive integer")
    return substring * n
if __name__ == '__main__':
    substring = "Hello"
    n1 = 3
    result1 = repeat_string(substring, n1)
    print(f"'{substring}' repeated {n1} times: '{result1}'")
    substring = "Python"
    n2 = 5
    result2 = repeat_string(substring, n2)
    print(f"'{substring}' repeated {n2} times: '{result2}'")
    try:
        repeat_string("Test", 0)
    except ValueError as e:
        print(f"Error caught for N=0: {e}")
    try:
        repeat_string("Test", -2)
    except ValueError as e:
        print(f"Error caught for N=-2: {e}")