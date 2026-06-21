def is_even(number):
    return (number & 1) == 0

class NumberChecker:
    def __init__(self, number):
        self.number = number
    
    def check_even(self):
        return is_even(self.number)

if __name__ == '__main__':
    test_values = [0, 1, 2, -3, 4, -5, 6, 7, 8, -9]
    for value in test_values:
        checker = NumberChecker(value)
        print(f"{value} is even: {checker.check_even()}")