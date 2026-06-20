class NumberSwapper:
    def __init__(self, num1, num2):
        self.numbers = [num1, num2]

    def swap(self):
        self.numbers[0], self.numbers[1] = self.numbers[1], self.numbers[0]
        return self.numbers

if __name__ == '__main__':
    swapper = NumberSwapper(5, 10)
    print("Before swap:", swapper.swap())