class TemperatureAnalyzer:

    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def calculate_difference(self):
        return abs(self.temp1 - self.temp2)
if __name__ == '__main__':
    sample_temp1 = 30.5
    sample_temp2 = 25.8
    analyzer = TemperatureAnalyzer(sample_temp1, sample_temp2)
    result = analyzer.calculate_difference()
    print(result)
    another_analyzer = TemperatureAnalyzer(45.0, 60.3)
    another_result = another_analyzer.calculate_difference()
    print(another_result)