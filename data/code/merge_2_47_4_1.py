import sys
def multiply_large_integers(num1: str, num2: str) -> int:
    if not num1 or not num2:
        return 0
    result = []
    for i in range(len(num1)):
        carry = 0
        for j in range(len(num2)):
            digit1 = ord(num1[i]) - ord('0')
            digit2 = ord(num2[j]) - ord('0')
            product = (digit1 * digit2) + carry
            result.append((product % 10))
            carry = product // 10
        if carry:
            while carry > 0:
                result.append(carry % 10)
                carry //= 10
    result.reverse()
    final_str = ''.join(str(digit) for digit in result).lstrip('0') or '0'
    return int(final_str)
if __name__ == '__main__':
    sample_num1 = "987654321"
    sample_num2 = "123456789"
    product_result = multiply_large_integers(sample_num1, sample_num2)
    print(product_result)