class Number:
    def __init__(self, value):
        self.value = value

    def subtract(self, other):
        return Number(self.value - other.value)

if __name__ == '__main__':
    num1 = Number(10)
    num2 = Number(5)
    result = num1.subtract(num2)
    print(f"num1: {num1.value}")
    print(f"num2: {num2.value}")
    print(f"result (num1 - num2): {result.value}")