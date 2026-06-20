class LargeIntegerMultiplier:
    BASE = 10

    @staticmethod
    def multiply(a: str, b: str) -> int:
        result = 0
        for i in range(len(b)):
            digit_b = int(b[len(b) - 1 - i])
            carry = 0
            temp_result = 0
            for j in range(len(a)):
                digit_a = int(a[len(a) - 1 - j])
                product = (digit_a * digit_b) + carry
                temp_result += product * LargeIntegerMultiplier.BASE ** j
                carry = product // LargeIntegerMultiplier.BASE
            result += temp_result * LargeIntegerMultiplier.BASE ** i
        return result

if __name__ == '__main__':
    multiplier = LargeIntegerMultiplier()
    num1 = '123456789'
    num2 = '987654321'
    product = multiplier.multiply(num1, num2)
    print(product)