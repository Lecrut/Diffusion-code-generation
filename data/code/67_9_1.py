class Adder:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calculate_sum(self):
        return self.a + self.b
if __name__ == '__main__':
    adder = Adder(10, 5)
    result = adder.calculate_sum()
    print(result)