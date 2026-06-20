def multiply_large_integers(a, b):
    result = 0
    for i in range(len(b)):
        digit = int(b[-i-1])
        carry = 0
        temp_result = 0
        for j in range(len(a)):
            num = int(a[-j-1])
            product = (num * digit) + carry
            temp_result += product % 10 * (10 ** j)
            carry = product // 10
        result += temp_result * (10 ** i)
    return result

if __name__ == '__main__':
    a = "12345678901234567890"
    b = "98765432109876543210"
    print(multiply_large_integers(a, b))