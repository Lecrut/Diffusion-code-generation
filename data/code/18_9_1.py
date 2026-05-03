class Number:
    def __init__(self, value):
        self.value = value
    def compare(self, other):
        return self.value > other.value
if __name__ == '__main__':
    num1 = Number(10)
    num2 = Number(5)
    num3 = Number(10)
    print(f"Is num1 greater than num2? {num1.compare(num2)}")
    print(f"Is num1 greater than num3? {num1.compare(num3)}")
    print(f"Is num2 greater than num1? {num2.compare(num1)}")
    print(f"Is num3 greater than num1? {num3.compare(num1)}")