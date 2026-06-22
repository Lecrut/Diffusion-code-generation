class StringLengthCalculator:
    def calculate(self, text):
        return len(text)

if __name__ == '__main__':
    calculator = StringLengthCalculator()
    sample_string = 'Hello World'
    print(calculator.calculate(sample_string))