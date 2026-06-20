class NumberAdder:
    def add_three_numbers(self, a, b, c):
        return a + b + c

if __name__ == '__main__':
    calculator = NumberAdder()
    result = calculator.add_three_numbers(5, 3, 8)
    print(result)