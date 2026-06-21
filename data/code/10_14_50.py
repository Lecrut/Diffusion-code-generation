class TemperatureComparer:
    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def compare(self):
        return max(self.temp1, self.temp2)

if __name__ == '__main__':
    sample_temp1 = 15.0
    sample_temp2 = 24.3
    comparer = TemperatureComparer(sample_temp1, sample_temp2)
    higher_temperature = comparer.compare()
    print(higher_temperature)