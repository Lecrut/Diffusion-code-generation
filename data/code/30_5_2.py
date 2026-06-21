def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    stack = []
    is_negative = decimal_number < 0
    number = abs(decimal_number)
    
    while number > 0:
        stack.append(str(number % 2))
        number = number // 2
    
    binary_str = ''.join(reversed(stack))
    
    if is_negative:
        binary_str = '-' + binary_str
    
    return binary_str

if __name__ == '__main__':
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(0))
    print(decimal_to_binary(-42))