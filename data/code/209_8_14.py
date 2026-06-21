import pandas as pd

class SeriesOperations:
    def __init__(self, data):
        self.series = pd.Series(data)
    
    def calculate_mean(self):
        return self.series.mean()

if __name__ == '__main__':
    analyzer = SeriesOperations([10, 20, 30, 40])
    mean_value = analyzer.calculate_mean()
    print(f"Mean of the series: {mean_value}")