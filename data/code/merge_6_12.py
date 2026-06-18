class Multiplier:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def get_product(self):
        return self.num1 * self.num2
if __name__ == '__main__':
    m = Multiplier(5, 10)
    result = m.get_product()
    print(result)