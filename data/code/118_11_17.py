def multiply_large_integers(a, b):
    result = 0
    for i in range(len(b)):
        digit_b = int(b[len(b) - 1 - i])
        carry = 0
        temp_result = 0
        for j in range(len(a)):
            digit_a = int(a[len(a) - 1 - j])
            product = (digit_a * digit_b) + carry
            temp_result += product * (10 ** j)
            carry = product // 10
        result += temp_result * (10 ** i)
    return str(result)

if __name__ == '__main__':
    num1 = 23456789
    num2 = 98765432
    result = multiply_large_integers(str(num1), str(num2))
    print(result)