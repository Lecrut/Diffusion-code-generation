class NumberChecker:
    def check_odd(self, number):
        return self.is_odd(number)

    def is_odd(self, n):
        return n % 2 != 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    sample_values = [10, 15, -6, 13, 22]
    results = [checker.check_odd(value) for value in sample_values]
    
    for value, result in zip(sample_values, results):
        print(f"{value} is odd: {result}")