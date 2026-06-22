class TemperatureAnalyzer:
    LESS_THAN = "is less than"
    GREATER_THAN = "is greater than"
    EQUAL_TO = "is equal to"

    @staticmethod
    def analyze(temp1, temp2):
        difference = abs(temp1 - temp2)
        if temp1 > temp2:
            magnitude = f"temp1 {TemperatureAnalyzer.GREATER_THAN} temp2"
        elif temp1 < temp2:
            magnitude = f"temp2 {TemperatureAnalyzer.GREATER_THAN} temp1"
        else:
            magnitude = f"both temperatures {TemperatureAnalyzer.EQUAL_TO}"
        return difference, magnitude

if __name__ == '__main__':
    sample_temp1 = 40
    sample_temp2 = 50
    diff, mag = TemperatureAnalyzer.analyze(sample_temp1, sample_temp2)
    print(f"Difference: {diff}")
    print(mag)