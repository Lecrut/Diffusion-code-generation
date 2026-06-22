class SumCalculator:
    @staticmethod
    def sum_numbers(**kwargs):
        total = 0.0
        for value in kwargs.values():
            total += value
        return total

if __name__ == '__main__':
    sample_values = {'num1': 1.5, 'num2': 2.75, 'num3': 3.0, 'num4': -4.2, 'num5': 10.1,
                     'num6': 5.0, 'num7': 2.0, 'num8': 3.5, 'num9': -1.2, 'num10': 4.3}
    result = SumCalculator.sum_numbers(**sample_values)
    print(result)