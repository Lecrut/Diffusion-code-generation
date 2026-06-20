def reverse_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    if a == 0 and b == 0:
        raise ValueError("Inputs cannot both be zero")

    while a != 0:
        temp = a
        a = b - (b // a) * a
        b = temp

    return b

if __name__ == '__main__':
    print(reverse_numbers(123456789, 987654321))