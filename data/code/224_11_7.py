class SequenceProcessor:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def calculate_average(self):
        return sum(self.sequence) / len(self.sequence)

if __name__ == '__main__':
    sample_sequence = [100, 200, 300]
    processor = SequenceProcessor(sample_sequence)
    average = processor.calculate_average()
    print(average)