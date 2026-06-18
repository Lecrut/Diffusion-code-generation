class NumberChecker:
    def check_parity(self, number):
        if isinstance(number, int) is False:
            raise TypeError("Input must be an integer.")
        
        return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample values to test the method without user input
    sample_numbers = [1, -4, 75, 0]
    
    for num in sample_numbers:
        result = checker.check_parity(num)
        print(f"{num} is {result}")