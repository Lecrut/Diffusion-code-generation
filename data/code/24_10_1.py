def is_negative(number):
    return number < 0
if __name__ == '__main__':
    print(f"is_negative(-5): {is_negative(-5)}")
    print(f"is_negative(0): {is_negative(0)}")
    print(f"is_negative(3.14): {is_negative(3.14)}")
    print(f"is_negative(-0.001): {is_negative(-0.001)}")
    print(f"is_negative(100): {is_negative(100)}")