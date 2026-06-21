def decimal_to_binary_stack(n):
    if n == 0:
        return '0'
    if n < 0:
        return '-' + decimal_to_binary_stack(-n)
    stack = []
    while n > 0:
        stack.append(n % 2)
        n = n // 2
    result = ''
    while stack:
        result += str(stack.pop())
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 5, 10, 255, 1024, -42]
    for value in sample_values:
        print(decimal_to_binary_stack(value))