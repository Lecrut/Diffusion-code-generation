class DataAnalyzer:
    @staticmethod
    def safe_mean(data):
        if not all(isinstance(item, (int, float)) for item in data):
            raise TypeError("Data list contains non-numeric types")
        return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    try:
        print(f"Mean of {sample_data}: {DataAnalyzer.safe_mean(sample_data)}")
    except TypeError as e:
        print(e)