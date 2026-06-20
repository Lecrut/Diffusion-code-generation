def check_even_odd(number):
    return number & 1 == 0
if __name__ == '__main__':
    print(check_even_odd(4))
    print(check_even_odd(5))