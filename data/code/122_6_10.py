class RunningAverageWelford:
    def __init__(self):
        self.count = 0
        self.mean = 0.0
        self.M2 = 0.0

    def add_value(self, value):
        self.count += 1
        delta = value - self.mean
        self.mean += delta / self.count
        delta2 = value - self.mean
        self.M2 += delta * delta2

    def get_mean(self):
        if self.count < 2:
            return None
        return self.mean

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    welford_avg = RunningAverageWelford()
    for value in sample_values:
        welford_avg.add_value(value)
    print(welford_avg.get_mean())