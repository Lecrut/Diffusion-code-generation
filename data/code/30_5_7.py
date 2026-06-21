def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    if decimal_number < 0:
        return "-" + decimal_to_binary(-decimal_number)
    stack = []
    n = decimal_number
    while n > 0:
        stack.append(n % 2)
        n = n // 2
    binary_string = ""
    while stack:
        binary_string += str(stack.pop())
    return binary_string

if __name__ == '__main__':
    print(decimal_to_binary(0))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-42))
    print(decimal_to_binary(1))