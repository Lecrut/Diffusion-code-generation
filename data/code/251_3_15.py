class DetermineTheLargestNumberPresentProcessor:
    def __init__(self):
        self.samples = []

    def add_sample(self, sample):
        if not isinstance(sample, list) or not all(isinstance(x, (int, float)) for x in sample):
            raise ValueError("Sample must be a list of numbers")
        self.samples.append(sample)

    def find_largest_number(self, sample_index=0):
        if sample_index < 0 or sample_index >= len(self.samples):
            raise IndexError("Invalid sample index")
        return max(self.samples[sample_index])

if __name__ == '__main__':
    processor = DetermineTheLargestNumberPresentProcessor()
    processor.add_sample([10, 5, 20, 8, 15])
    processor.add_sample([-5, -1, -10, -3])
    processor.add_sample([42])
    print(f"Largest number in first sample: {processor.find_largest_number(0)}")
    print(f"Largest number in second sample: {processor.find_largest_number(1)}")
    print(f"Largest number in third sample: {processor.find_largest_number(2)}")