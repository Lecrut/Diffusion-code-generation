class MathUtils:
    @staticmethod
    def is_positive(number: float) -> bool:
        return number > 0
if __name__ == '__main__':
    value1 = 10.5
    value2 = -5.2
    value3 = 0.0
    value4 = 1.0
    print(f"Is {value1} positive? {MathUtils.is_positive(value1)}")
    print(f"Is {value2} positive? {MathUtils.is_positive(value2)}")
    print(f"Is {value3} positive? {MathUtils.is_positive(value3)}")
    print(f"Is {value4} positive? {MathUtils.is_positive(value4)}")