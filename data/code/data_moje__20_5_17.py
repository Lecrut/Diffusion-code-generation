def check_even(n):
    return "even" if n % 2 == 0 else "odd"

if __name__ == '__main__':
    print(check_even(4))
    print(check_even(7))
    print(check_even(100))
    print(check_even(101))