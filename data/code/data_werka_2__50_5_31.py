class NonNegativeDifferencer:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def get_difference(self):
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    differencer = NonNegativeDifferencer(50, 23)
    print(differencer.get_difference())