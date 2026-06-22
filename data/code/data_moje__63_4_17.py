def reverse_integer(n):
    if n < 0:
        negative = True
        n = -n
    else:
        negative = False
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    if negative:
        return -reversed_num
    return reversed_num

if __name__ == '__main__':
    sample_value = 12345
    result = reverse_integer(sample_value)
    print(result)
    sample_negative = -9876
    result_neg = reverse_integer(sample_negative)
    print(result_neg)