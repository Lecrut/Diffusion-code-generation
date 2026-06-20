def multiply_large_integers(a: str, b: str) -> str:
    result = [0] * (len(a) + len(b))
    for i in range(len(a) - 1, -1, -1):
        carry = 0
        for j in range(len(b) - 1, -1, -1):
            product = int(a[i]) * int(b[j]) + carry + result[i + j + 1]
            result[i + j + 1] = product % 10
            carry = product // 10
        result[i + j] += carry

    final_result = ''
    for digit in result:
        if not final_result and digit == 0:
            continue
        final_result += str(digit)

    return '0' if not final_result else final_result

if __name__ == '__main__':
    print(multiply_large_integers('123456789', '987654321'))