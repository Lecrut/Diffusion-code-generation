def reverse_integer(n):
    negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    if negative:
        reversed_num = -reversed_num
    return reversed_num

if __name__ == '__main__':
    sample_inputs = [123, -456, 120, 0, -987654321]
    for value in sample_inputs:
        result = reverse_integer(value)
        print(result)