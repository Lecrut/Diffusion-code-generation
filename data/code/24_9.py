class MathUtils:
    @staticmethod
    def is_negative(number: float) -> bool:
        return number < 0
if __name__ == '__main__':
    value1 = -5.0
    value2 = 10.5
    value3 = 0.0
    value4 = -0.001
    print(f"Is {value1} negative? {MathUtils.is_negative(value1)}")
    print(f"Is {value2} negative? {MathUtils.is_negative(value2)}")
    print(f"Is {value3} negative? {MathUtils.is_negative(value3)}")
    print(f"Is {value4} negative? {MathUtils.is_negative(value4)}")