class DataAnalyzer:
    @staticmethod
    def calculate_mean(values):
        if not values:
            raise ValueError("The list is empty")
        return sum(values) / len(values)

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data = [5, 10, 15, 20]
    mean_value = analyzer.calculate_mean(sample_data)
    print(f"The mean of {sample_data} is {mean_value}")