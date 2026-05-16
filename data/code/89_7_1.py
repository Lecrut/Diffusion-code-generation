from abc import ABC, abstractmethod
class Operation(ABC):
    @abstractmethod
    def evaluate(self, a, b):
        pass
class Addition(Operation):
    def evaluate(self, a, b):
        return a + b
class Multiplication(Operation):
    def evaluate(self, a, b):
        return a * b
if __name__ == '__main__':
    add_op = Addition()
    mul_op = Multiplication()
    num1 = 10
    num2 = 5
    result_add = add_op.evaluate(num1, num2)
    result_mul = mul_op.evaluate(num1, num2)
    print(f"Addition result: {result_add}")
    print(f"Multiplication result: {result_mul}")