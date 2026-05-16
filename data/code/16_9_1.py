class MathUtils:
    @staticmethod
    def is_positive(number):
        return number > 0
if __name__ == '__main__':
    value1 = 10
    value2 = -5
    value3 = 0
    value4 = 3.14
    print(f"Is {value1} positive? {MathUtils.is_positive(value1)}")
    print(f"Is {value2} positive? {MathUtils.is_positive(value2)}")
    print(f"Is {value3} positive? {MathUtils.is_positive(value3)}")
    print(f"Is {value4} positive? {MathUtils.is_positive(value4)}")