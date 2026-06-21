class SumCalculator:
    @staticmethod
    def is_numeric(value):
        return isinstance(value, (int, float))

    def sum_values(self, values):
        if not hasattr(values, '__iter__'):
            raise TypeError("Input is not iterable")
        
        total = 0
        for value in values:
            if self.is_numeric(value):
                total += value
            else:
                raise ValueError(f"Non-numeric value encountered: {value}")
        
        return total

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_values = [1, 2, 3.5, 4]
    try:
        result = calculator.sum_values(sample_values)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)