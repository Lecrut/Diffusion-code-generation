def reverse_integer(n):
    if n < 0:
        return -int(str(-n)[::-1])
    else:
        return int(str(n)[::-1])

if __name__ == '__main__':
    test_values = [123, -456, 0, 120, -120, 1000000003, -2147483648]
    for val in test_values:
        print(f"Input: {val}, Reversed: {reverse_integer(val)}")