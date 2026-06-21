def integer_to_binary(n):
    if n == 0:
        return "0"
    negative = False
    if n < 0:
        negative = True
        n = -n
    bits = []
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder))
        n = n // 2
    result = "".join(bits[::-1])
    if negative:
        result = "-" + result
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 5, 10, 255, -42, 1024]
    for value in sample_values:
        print(integer_to_binary(value))