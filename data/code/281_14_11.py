class NumberSum:
    NUMBERS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    
    @staticmethod
    def calculate_sum(numbers):
        return sum(numbers)
    
if __name__ == '__main__':
    calculator = NumberSum()
    total_sum = calculator.calculate_sum(NumberSum.NUMBERS)
    print(total_sum)