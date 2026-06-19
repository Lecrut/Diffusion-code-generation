class NumberSummer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_sum(self):
        try:
            num1 = float(self.a)
            num2 = float(self.b)
            return num1 + num2
        except ValueError:
            return "Error: Invalid input. Please enter numeric values."

if __name__ == '__main__':
    summer1 = NumberSummer(10, 5)
    print(summer1.calculate_sum())

    summer2 = NumberSummer("hello", 5)
    print(summer2.calculate_sum())

    summer3 = NumberSummer(3.5, 2.1)
    print(summer3.calculate_sum())

    summer4 = NumberSummer("a", "b")
    print(summer4.calculate_sum())