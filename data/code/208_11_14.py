class MeanCalculator:
    def calculate_mean(self, data):
        if not data:
            return None
        return sum(data) / len(data)

if __name__ == '__main__':
    calculator = MeanCalculator()
    sample_data = [10, 20.5, 30, 40.75]
    mean_value = calculator.calculate_mean(sample_data)
    print(mean_value)