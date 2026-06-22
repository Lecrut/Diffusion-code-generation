def reverse_integer(n):
    is_negative = n < 0
    s = str(abs(n))
    reversed_s = s[::-1]
    result = int(reversed_s)
    if is_negative:
        result = -result
    return result

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-6789))
    print(reverse_integer(0))
    print(reverse_integer(1200))
    print(reverse_integer(-90))