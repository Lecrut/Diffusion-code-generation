class NumberChecker:
    def check_odd(self, number):
        return number % 2 != 0

if __name__ == '__main__':
    ODD_CHECKER = NumberChecker()
    SAMPLE_NUMBERS = [15, 28, 39]
    
    for number in SAMPLE_NUMBERS:
        is_odd = ODD_CHECKER.check_odd(number)
        print(f"The number {number} is odd: {is_odd}")