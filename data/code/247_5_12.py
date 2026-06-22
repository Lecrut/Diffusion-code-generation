class Adder:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_sum(self):
        return self.a + self.b

if __name__ == '__main__':
    adder_instance = Adder(5, 3)
    print(adder_instance.calculate_sum())