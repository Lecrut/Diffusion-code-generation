class PeakFinder:
    @staticmethod
    def find_peak(sequence):
        return max(sequence)

if __name__ == '__main__':
    sample_sequence = [15, 27, 9, 34, 8]
    peak_value = PeakFinder.find_peak(sample_sequence)
    print(peak_value)