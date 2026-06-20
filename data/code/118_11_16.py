class LargeIntegerMultiplier:

    def __init__(self):
        self.BASE = 10

    def multiply(self, a: str, b: str) -> str:
        result = [0] * (len(a) + len(b))
        for i in range(len(a) - 1, -1, -1):
            carry = 0
            for j in range(len(b) - 1, -1, -1):
                prod = int(a[i]) * int(b[j]) + result[i + j + 1] + carry
                carry = prod // self.BASE
                result[i + j + 1] = prod % self.BASE
            result[i + j] += carry
        while len(result) > 1 and result[0] == 0:
            result.pop(0)
        return ''.join(map(str, result))
if __name__ == '__main__':
    multiplier = LargeIntegerMultiplier()
    num1 = '123456789'
    num2 = '987654321'
    result = multiplier.multiply(num1, num2)
    print(result)