import pandas as pd

class SeriesStatistics:
    def __init__(self, data):
        self.series = pd.Series(data)
    
    def compute_mean(self):
        return self.series.mean()

if __name__ == '__main__':
    analyzer = SeriesStatistics([10, 20, 30, 40])
    mean_value = analyzer.compute_mean()
    print(f"The mean of the series is: {mean_value}")