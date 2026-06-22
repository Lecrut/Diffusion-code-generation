class SumCalculator:
    @staticmethod
    def sum_numbers(**kwargs):
        total = 0.0
        for number in kwargs.values():
            total += number
        return total

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.sum_numbers(num1=1.5, num2=2.75, num3=3.0, num4=-4.2, num5=10.1,
                                   num6=1.5, num7=2.75, num8=3.0, num9=-4.2, num10=10.1)
    print(result)