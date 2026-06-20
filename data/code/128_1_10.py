class NumberChecker:
    def __init__(self):
        self.numbers = [-5, 0, 10.5, -0.001]

    def check_negativity(self):
        return [num < 0 for num in self.numbers]

if __name__ == '__main__':
    checker = NumberChecker()
    results = checker.check_negativity()
    print(results)