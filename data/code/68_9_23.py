class NumberProcessor:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def find_difference(self):
        return abs(self.num1 - self.num2)

if __name__ == '__main__':
    processor1 = NumberProcessor(10, 4)
    print(processor1.find_difference())

    processor2 = NumberProcessor(-5, 15)
    print(processor2.find_difference())

    processor3 = NumberProcessor(7.5, 3.2)
    print(processor3.find_difference())

    processor4 = NumberProcessor(0, 0)
    print(processor4.find_difference())