class NumberUtil:
    @staticmethod
    def is_odd(number: int) -> bool:
        return number & 1 == 1

if __name__ == '__main__':
    num1 = 7
    num2 = 10
    num3 = 0
    num4 = -3
    print(f"Is {num1} odd? {NumberUtil.is_odd(num1)}")
    print(f"Is {num2} odd? {NumberUtil.is_odd(num2)}")
    print(f"Is {num3} odd? {NumberUtil.is_odd(num3)}")
    print(f"Is {num4} odd? {NumberUtil.is_odd(num4)}")