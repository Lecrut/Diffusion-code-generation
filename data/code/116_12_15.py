class Summation:
    def add(self, x: float, y: float, z: float) -> float:
        return x + y + z

if __name__ == '__main__':
    calculator = Summation()
    num1 = 10.5
    num2 = 20.75
    num3 = -5.25
    result = calculator.add(num1, num2, num3)
    print(result)