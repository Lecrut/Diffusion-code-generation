class TemperatureAnalyzer:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def calculate_difference(self):
        return abs(self.temp1 - self.temp2)

    def determine_magnitude(self):
        if self.temp1 > self.temp2:
            return "First temperature is greater"
        elif self.temp1 < self.temp2:
            return "Second temperature is greater"
        else:
            return "Both temperatures are equal"

if __name__ == '__main__':
    temp_analyzer = TemperatureAnalyzer(30, 25)
    difference = temp_analyzer.calculate_difference()
    magnitude = temp_analyzer.determine_magnitude()
    print(f"Difference: {difference}")
    print(magnitude)