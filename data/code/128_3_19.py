def validate_input(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be an integer or float")

def is_negative(num):
    validate_input(num)
    return num < 0

if __name__ == '__main__':
    print(is_negative(-5))
    print(is_negative(0))
    print(is_negative(3.14))