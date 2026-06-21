def integer_to_binary(n):
    if n == 0:
        return "0"
    if n < 0:
        return "-" + integer_to_binary(-n)
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
    binary_digits.reverse()
    return "".join(binary_digits)

if __name__ == '__main__':
    print(integer_to_binary(0))
    print(integer_to_binary(5))
    print(integer_to_binary(10))
    print(integer_to_binary(255))
    print(integer_to_binary(-10))