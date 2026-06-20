class ArithmeticCalculator:
    ADD = "add"
    SUBTRACT = "subtract"

    @staticmethod
    def perform_operation(operation, numbers):
        if operation == ArithmeticCalculator.ADD:
            return sum(numbers)
        elif operation == ArithmeticCalculator.SUBTRACT:
            result = numbers[0]
            for number in numbers[1:]:
                result -= number
            return result
        else:
            raise ValueError("Invalid operation")

if __name__ == '__main__':
    calculator = ArithmeticCalculator()
    print(calculator.perform_operation(ArithmeticCalculator.ADD, [5, 3]))
    print(calculator.perform_operation(ArithmeticCalculator.SUBTRACT, [10, 2]))