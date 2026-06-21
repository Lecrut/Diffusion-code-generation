def sum_values(values):
    if not hasattr(values, '__iter__'):
        raise TypeError("Input is not iterable")
    total = 0
    for value in values:
        if isinstance(value, (int, float)):
            total += value
        else:
            raise ValueError(f"Non-numeric value encountered: {value}")
    return total

class SumCalculator:
    def sum_values(self, values):
        return sum_values(values)

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_values = [10, 20.5, 30, "40"]
    try:
        result = calculator.sum_values(sample_values)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)