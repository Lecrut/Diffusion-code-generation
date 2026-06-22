def decimal_to_binary_using_stack(n):
    if n == 0:
        return "0"
    if n < 0:
        return "-" + decimal_to_binary_using_stack(-n)
    stack = []
    while n > 0:
        stack.append(str(n % 2))
        n = n // 2
    result = "".join(reversed(stack))
    return result

if __name__ == '__main__':
    print(decimal_to_binary_using_stack(10))
    print(decimal_to_binary_using_stack(255))
    print(decimal_to_binary_using_stack(0))
    print(decimal_to_binary_using_stack(1))
    print(decimal_to_binary_using_stack(-42))