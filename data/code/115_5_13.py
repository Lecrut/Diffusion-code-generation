class ElementWiseDivider:
    @staticmethod
    def divide_lists(dividends, divisors):
        if len(dividends) != len(divisors):
            raise ValueError("Lists must be of equal length")
        
        return [dividend / divisor for dividend, divisor in zip(dividends, divisors)]

if __name__ == '__main__':
    dividends = [10, 15, 7]
    divisors = [2, 3, 0]
    
    try:
        result = ElementWiseDivider.divide_lists(dividends, divisors)
        print(result)
    except ValueError as e:
        print(f"Error caught: {e}")