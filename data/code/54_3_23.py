from typing import List

def calculate_sum(numbers: List[int]) -> int:
    return sum(numbers)

def calculate_product(numbers: List[int]) -> int:
    product = 1
    for number in numbers:
        product *= number
    return product

class Calculator:
    def __init__(self, values: List[int]):
        self.values = values
    
    def add(self) -> int:
        return sum(self.values)
    
    def multiply(self) -> int:
        product = 1
        for value in self.values:
            product *= value
        return product

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print("Sum of sample numbers:", calculate_sum(sample_numbers))
    print("Product of sample numbers:", calculate_product(sample_numbers))
    
    calculator_instance = Calculator([6, 7, 8])
    print("Addition using Calculator instance:", calculator_instance.add())
    print("Multiplication using Calculator instance:", calculator_instance.multiply())