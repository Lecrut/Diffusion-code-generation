def reverse_integer(n):
    negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    if negative:
        reversed_num = -reversed_num
    return reversed_num

if __name__ == '__main__':
    sample_values = [123, -456, 7890, 120, 0, -1]
    for val in sample_values:
        print(reverse_integer(val))