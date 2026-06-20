class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    @staticmethod
    def compute_operations(a, b):
        add_result = Calculator().add(a, b)
        subtract_result = Calculator().subtract(a, b)
        print(f"Sum: {add_result}")
        print(f"Difference: {subtract_result}")

if __name__ == '__main__':
    Calculator.compute_operations(10, 5)