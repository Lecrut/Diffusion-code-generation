def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n < 0:
        return "-" + decimal_to_binary(-n)
    stack = []
    while n > 0:
        stack.append(n % 2)
        n = n // 2
    result = ""
    while stack:
        result += str(stack.pop())
    return result

if __name__ == "__main__":
    print(decimal_to_binary(0))
    print(decimal_to_binary(5))
    print(decimal_to_binary(10))
    print(decimal_to_binary(255))
    print(decimal_to_binary(-13))