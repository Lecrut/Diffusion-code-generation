class IterativeFactorial:
    def __init__(self):
        self.name = "IterativeFactorial"

    def get_result(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        if number < 0:
            raise ValueError("Input must be non-negative")
        
        accumulator = 1
        current = 2
        
        while current <= number:
            accumulator *= current
            current += 1
            
        return accumulator

if __name__ == '__main__':
    calculator_instance = IterativeFactorial()
    test_cases = [0, 1, 5, 7, 12]
    for case in test_cases:
        computed_value = calculator_instance.get_result(case)
        print(computed_value)