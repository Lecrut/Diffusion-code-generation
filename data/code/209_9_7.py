def average_sample(sample):
    return sum(x for x in sample) / len(sample)

class SampleAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def compute_average(self):
        return average_sample(self.data)
    
    def get_data_size(self):
        return len(self.data)

if __name__ == '__main__':
    analyzer = SampleAnalyzer([50, 60, 70])
    avg = analyzer.compute_average()
    size = analyzer.get_data_size()
    print(f"Average: {avg}, Data Size: {size}")