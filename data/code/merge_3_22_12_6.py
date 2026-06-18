class NumberChecker:
    def check_odd(self, number):
        return bool(number % 2)

if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [10, 7, -3, 0]
    
    for val in test_values:
        result = checker.check_odd(val)
        print(f"{val} is {'odd' if result else 'even'}")