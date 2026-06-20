def multiply_large_integers(a, b):
    result = 0
    for i in range(len(b)):
        digit_b = int(b[-(i + 1)])
        carry = 0
        temp_result = 0
        for j in range(len(a)):
            digit_a = int(a[-(j + 1)])
            product = (digit_a * digit_b) + carry
            temp_result += product * (10 ** j)
            carry = product // 10
        result += temp_result * (10 ** i)
    return str(result)

if __name__ == '__main__':
    print(multiply_large_integers('12345678901234567890', '98765432109876543210'))