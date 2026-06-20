class RunningAverage:
    def __init__(self):
        self.count = 0
        self.mean = 0.0
        self.m2 = 0.0

    @staticmethod
    def update(average, value):
        average.count += 1
        delta = value - average.mean
        average.mean += delta / average.count
        delta2 = value - average.mean
        average.m2 += delta * delta2

    def get_mean(self):
        if self.count < 1:
            return None
        return self.mean

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    average = RunningAverage()
    for value in sample_values:
        RunningAverage.update(average, value)
    print("Running Average:", average.get_mean())