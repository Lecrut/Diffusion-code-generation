def decimal_to_binary(number):
    if number == 0:
        return '0'
    is_negative = number < 0
    number = abs(number)
    bits = []
    while number > 0:
        bits.append(str(number & 1))
        number >>= 1
    bits.reverse()
    result = ''.join(bits)
    if is_negative:
        result = '-' + result
    return result

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(10))
    print(decimal_to_binary(15))
    print(decimal_to_binary(-10))
    print(decimal_to_binary(2**100))