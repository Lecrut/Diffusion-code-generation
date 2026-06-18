class NumberChecker:
    def check_parity(self, number):
        if number % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample inputs with hard-coded values
    test_numbers = [10, 7, -4, 3.5] 
    
    for num in test_numbers:
        if isinstance(num, int):
            result = checker.check_parity(num)
            print(f"Number {num} is {result}")
        else:
            print(f"{num} cannot be checked as it is not an integer")