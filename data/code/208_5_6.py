class MeanCalculator:
    @staticmethod
    def calculate_mean(data):
        return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(f"Mean of {sample_data}: {MeanCalculator.calculate_mean(sample_data)}")