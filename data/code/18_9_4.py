class Number:
    def __init__(self, value):
        self.value = value
    def compare(self, other):
        if self.value > other.value:
            return 1
        elif self.value < other.value:
            return -1
        else:
            return 0
if __name__ == '__main__':
    num1 = Number(10)
    num2 = Number(20)
    num3 = Number(10)
    result1 = num1.compare(num2)
    print(f"Comparison between 10 and 20: {result1}")
    result2 = num2.compare(num1)
    print(f"Comparison between 20 and 10: {result2}")
    result3 = num1.compare(num3)
    print(f"Comparison between 10 and 10: {result3}")