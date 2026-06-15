class QuantityAdder:
    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    adder = QuantityAdder()
    num1 = 10
    num2 = 5
    result = adder.add(num1, num2)
    print(result)