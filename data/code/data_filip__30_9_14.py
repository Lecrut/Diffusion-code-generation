def binary_to_decimal(binary_str):
    if not binary_str:
        return 0
    result = 0
    power = 1
    for index in range(len(binary_str) - 1, -1, -1):
        digit = binary_str[index]
        if digit == '1':
            result += power
        power *= 2
    return result

def decimal_to_binary_manual(n):
    if n == 0:
        return '0'
    bits = []
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder))
        n = n // 2
    bits.reverse()
    return ''.join(bits)

if __name__ == '__main__':
    test_values = [0, 1, 2, 5, 10, 42, 255, 1024]
    for value in test_values:
        binary_rep = decimal_to_binary_manual(value)
        recovered_value = binary_to_decimal(binary_rep)
        print(f"Decimal: {value} -> Binary: {binary_rep} -> Recovered: {recovered_value}")