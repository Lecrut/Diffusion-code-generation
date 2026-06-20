class DivisionCalculator:
    @staticmethod
    def divide_lists(dividends, divisors):
        if len(dividends) != len(divisors):
            raise ValueError("Dividends and divisors lists must be of the same length")
        
        return [dividend / divisor for dividend, divisor in zip(dividends, divisors)]

if __name__ == '__main__':
    dividends = [10, 15, 7]
    divisors = [2, 3, 0]
    
    calculator = DivisionCalculator()
    try:
        result = calculator.divide_lists(dividends, divisors)
        print(f"Quotients: {result}")
    except ValueError as e:
        print(f"Error caught: {e}")