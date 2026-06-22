def reverse_integer(n: int) -> int:
    negative = n < 0
    n = abs(n)
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    if negative:
        reversed_n = -reversed_n
    return reversed_n

if __name__ == '__main__':
    samples = [123, -456, 1200, 0, -7, 987654321]
    for sample in samples:
        print(f"reverse_integer({sample}) = {reverse_integer(sample)}")