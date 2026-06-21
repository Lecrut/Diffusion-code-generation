class NumberProcessor:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def divide(self):
        try:
            result = self.num1 / self.num2
            return result
        except ZeroDivisionError as e:
            print(f"Error: Division by zero is not allowed.")
            return None

if __name__ == '__main__':
    processor = NumberProcessor(10, 0)
    result = processor.divide()
    if result is not None:
        print(f"The division result is {result}")