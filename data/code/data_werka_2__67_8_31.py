class Adder:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        if not all(isinstance(i, (int, float)) for i in [a, b]):
            raise ValueError("Both arguments must be numbers")
        self.result = a + b
        return self.result

if __name__ == '__main__':
    adder = Adder()
    print(adder.add(15, 25))
    print(adder.add(-5, 10))