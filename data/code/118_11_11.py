class LargeNumberMultiplier:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for i in range(len(num2)):
            digit_b = int(num2[len(num2) - 1 - i])
            carry = 0
            temp_result = 0
            for j in range(len(num1)):
                digit_a = int(num1[len(num1) - 1 - j])
                product = (digit_a * digit_b) + carry
                temp_result += product * (10 ** j)
                carry = product // 10
            result += temp_result * (10 ** i)
        return str(result)

if __name__ == '__main__':
    multiplier = LargeNumberMultiplier()
    print(multiplier.multiply('123456789', '987654321'))