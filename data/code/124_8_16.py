class ArithmeticOperations:
    def add_with_bitwise(self, a, b):
        while b != 0:
            carry = a & b
            a ^= b
            b <<= 1
        return a

    def multiply_with_bitwise(self, a, b):
        result = 0
        if a < 0:
            a = -a
            b = -b
        while b > 0:
            if b & 1 == 1:
                result += a
            a <<= 1
            b >>= 1
        return result

    def divide_with_bitwise(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        sign = -1 if ((a < 0) ^ (b < 0)) else 1
        a, b = abs(a), abs(b)
        quotient = 0
        temp = 0

        for i in range(31, -1, -1):
            if temp + (b << i) <= a:
                temp += b << i
                quotient |= 1 << i

        return sign * quotient

    def subtract_with_bitwise(self, a, b):
        return self.add_with_bitwise(a, ~b)

if __name__ == '__main__':
    ao = ArithmeticOperations()
    print((ao.add_with_bitwise(10, 5), ao.subtract_with_bitwise(10, 5),
            ao.multiply_with_bitwise(10, 5), ao.divide_with_bitwise(10, 2)))