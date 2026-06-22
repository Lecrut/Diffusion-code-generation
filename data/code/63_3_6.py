import sys

class IntegerReverser:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1

    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        num = abs(x)
        reversed_num = 0
        while num != 0:
            digit = num % 10
            num //= 10
            if reversed_num > self.INT_MAX // 10 or (reversed_num == self.INT_MAX // 10 and digit > 7):
                return 0
            reversed_num = reversed_num * 10 + digit
        result = sign * reversed_num
        if result < self.INT_MIN or result > self.INT_MAX:
            return 0
        return result

if __name__ == '__main__':
    reverser = IntegerReverser()
    print(reverser.reverse(123))
    print(reverser.reverse(-456))
    print(reverser.reverse(0))
    print(reverser.reverse(1534236469))