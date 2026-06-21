class MeanCalculator:
    @staticmethod
    def calculate_mean(data):
        if not data:
            return None
        return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [10, 20.5, 30, 40.75]
    mean_value = MeanCalculator.calculate_mean(sample_data)
    print(mean_value)