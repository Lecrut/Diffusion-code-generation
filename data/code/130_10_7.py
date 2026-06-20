def is_zero(number):
    return number == 0

if __name__ == '__main__':
    print(f"is_zero(0): {is_zero(0)}")
    print(f"is_zero(5): {is_zero(5)}")
    print(f"is_zero(-0): {is_zero(-0)}")
    print(f"is_zero(3.14): {is_zero(3.14)}")