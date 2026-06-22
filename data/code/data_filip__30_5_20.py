def decimal_to_binary_stack(n):
    if n < 0:
        raise ValueError("Only non-negative integers are supported")
    if n == 0:
        return "0"
    stack = []
    while n > 0:
        stack.append(n % 2)
        n = n // 2
    binary_digits = []
    while stack:
        binary_digits.append(str(stack.pop()))
    return "".join(binary_digits)

if __name__ == '__main__':
    print(decimal_to_binary_stack(10))
    print(decimal_to_binary_stack(0))
    print(decimal_to_binary_stack(255))
    print(decimal_to_binary_stack(1))
    print(decimal_to_binary_stack(42))