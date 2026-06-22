def reverse_integer(n: int) -> int:
    neg = n < 0
    digits = []
    n = abs(n)
    while n > 0:
        digits.append(str(n % 10))
        n //= 10
    reversed_str = "".join(digits)
    if reversed_str == "":
        return 0
    reversed_int = int(reversed_str)
    if neg:
        reversed_int = -reversed_int
    limit = 2**31
    if reversed_int >= limit or reversed_int < -limit:
        return 0
    return reversed_int

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-456))
    print(reverse_integer(120))
    print(reverse_integer(0))