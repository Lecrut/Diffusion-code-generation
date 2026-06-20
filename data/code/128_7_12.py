class NegativeCheck:
    def check_negative(self, value):
        return value < 0

if __name__ == '__main__':
    checker = NegativeCheck()
    sample_values = [-5, 3, -2, 7]
    for value in sample_values:
        if checker.check_negative(value):
            print(f"{value} is negative")
        else:
            print(f"{value} is not negative")