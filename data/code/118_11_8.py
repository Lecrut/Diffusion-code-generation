MAX_DIGIT = 10

def multiply_large_integers(a: str, b: str) -> int:
    result = 0
    for i, digit_b in enumerate(reversed(b)):
        carry = 0
        temp_result = 0
        for j, digit_a in enumerate(reversed(a)):
            product = (int(digit_a) * int(digit_b)) + carry
            temp_result += product * (MAX_DIGIT ** j)
            carry = product // MAX_DIGIT
        result += temp_result * (MAX_DIGIT ** i)
    return result

if __name__ == '__main__':
    num1 = '123456789'
    num2 = '987654321'
    print(multiply_large_integers(num1, num2))