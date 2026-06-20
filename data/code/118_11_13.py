def multiply_large_integers(a, b):
    result = 0
    for i in range(len(b)):
        digit_b = int(b[len(b) - 1 - i])
        carry = 0
        temp_result = 0
        multiplier = 10 ** i
        for j in range(len(a)):
            digit_a = int(a[len(a) - 1 - j])
            product = (digit_a * digit_b) + carry
            temp_result += product * multiplier
            carry = product // 10
        result += temp_result
    return result

if __name__ == '__main__':
    num1 = '123456789'
    num2 = '987654321'
    result = multiply_large_integers(num1, num2)
    print(result)