def reverse_binary_conversion(number):
    if number == 0:
        return "0"
    negative = False
    if number < 0:
        negative = True
        number = -number
    binary_digits = []
    while number > 0:
        remainder = number % 2
        binary_digits.append(str(remainder))
        number = number // 2
    binary_digits.reverse()
    result = "".join(binary_digits)
    if negative:
        result = "-" + result
    return result

if __name__ == '__main__':
    print(reverse_binary_conversion(10))
    print(reverse_binary_conversion(255))
    print(reverse_binary_conversion(0))
    print(reverse_binary_conversion(1))
    print(reverse_binary_conversion(-42))