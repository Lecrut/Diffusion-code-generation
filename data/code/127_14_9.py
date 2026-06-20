class NumberUtils:
    @staticmethod
    def is_odd(n):
        return n & 1

if __name__ == '__main__':
    num1 = 7
    num2 = 10
    num3 = 0
    print(f"Is {num1} odd? {NumberUtils.is_odd(num1)}")
    print(f"Is {num2} odd? {NumberUtils.is_odd(num2)}")
    print(f"Is {num3} odd? {NumberUtils.is_odd(num3)}")