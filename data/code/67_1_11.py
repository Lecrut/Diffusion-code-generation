class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    NUM1 = 7
    NUM2 = 13
    calc = Calculator()
    result = calc.add(NUM1, NUM2)
    print(result)