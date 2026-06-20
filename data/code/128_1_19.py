NEGATIVE_THRESHOLD = 0

def is_negative(number):
    return number < NEGATIVE_THRESHOLD

if __name__ == '__main__':
    print(f"is_negative(-5): {is_negative(-5)}")
    print(f"is_negative(0): {is_negative(0)}")
    print(f"is_negative(10.5): {is_negative(10.5)}")
    print(f"is_negative(-0.001): {is_negative(-0.001)}")