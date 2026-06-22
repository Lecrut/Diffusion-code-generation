def reverse_integer(n):
    sign = 1
    if n < 0:
        sign = -1
        n = -n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return sign * reversed_num

if __name__ == '__main__':
    sample_inputs = [123, -456, 0, 9870, -100]
    for value in sample_inputs:
        result = reverse_integer(value)
        print(f"{value} -> {result}")