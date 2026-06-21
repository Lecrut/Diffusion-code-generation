class SampleAnalyzer:
    def __init__(self, sample):
        self.sample = sample
    
    def compute_average(self):
        return sum(x for x in self.sample) / len(self.sample)

if __name__ == '__main__':
    analyzer = SampleAnalyzer([50, 60, 70])
    avg = analyzer.compute_average()
    print(avg)