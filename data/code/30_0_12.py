def int_to_binary(n):
    if n == 0:
        return "0"
    result = []
    while n > 0:
        result.append(str(n & 1))
        n >>= 1
    return "".join(reversed(result))

if __name__ == '__main__':
    test_values = [0, 1, 2, 10, 42, 1000, 65535]
    for val in test_values:
        print(f"{val}: {int_to_binary(val)}")