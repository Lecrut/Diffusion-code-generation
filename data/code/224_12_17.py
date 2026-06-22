class Calculator:
    @staticmethod
    def calculate_mean(values):
        return sum(values) / len(values)

if __name__ == '__main__':
    calculator = Calculator()
    sample_values = [5, 10, 15, 20]
    mean_value = calculator.calculate_mean(sample_values)
    print(mean_value)