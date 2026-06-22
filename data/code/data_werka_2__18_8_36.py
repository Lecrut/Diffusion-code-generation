class Number:
    def __init__(self, value):
        self.value = value

    def compare(self, other):
        if not isinstance(other, Number):
            raise ValueError('Argument must be an instance of Number')
        return self.value == other.value

if __name__ == '__main__':
    num1 = Number(5)
    num2 = Number(5)
    num3 = Number(10)

    comparison_results = {
        'num1 vs num2': num1.compare(num2),
        'num1 vs num3': num1.compare(num3)
    }

    for description, result in comparison_results.items():
        print(f'{description}: {result}')