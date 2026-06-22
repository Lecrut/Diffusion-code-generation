def decimal_to_binary(n):
    if n == 0:
        return '0'
    negative = False
    if n < 0:
        negative = True
        n = -n
    bits = []
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder))
        n = n >> 1
    if negative:
        bits.append('-')
    return ''.join(reversed(bits))

if __name__ == '__main__':
    result = decimal_to_binary(10)
    print(result)