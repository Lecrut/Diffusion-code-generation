class NumberChecker:
    def check_positivity(self, value):
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    test_values = [-5, 0, 3.14]
    
    for val in test_values:
        result = checker.check_positivity(val)
        print(f"Is {val} positive? {result}")