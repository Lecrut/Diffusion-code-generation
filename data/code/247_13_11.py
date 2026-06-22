class IntegerSumCalculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both inputs must be integers")
        self.result = a + b
        return self.result

if __name__ == '__main__':
    calc = IntegerSumCalculator()
    try:
        result = calc.add(5, 3)
        print(result)
    except ValueError as e:
        print(e)