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
    mult_op = Multiplication()
    a_val = 10
    b_val = 5
    result_add = add_op.evaluate(a_val, b_val)
    result_mult = mult_op.evaluate(a_val, b_val)
    print(f"Addition of {a_val} and {b_val}: {result_add}")
    print(f"Multiplication of {a_val} and {b_val}: {result_mult}")