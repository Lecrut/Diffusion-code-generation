class MiddleElementFinder:
    @staticmethod
    def find_middle(sequence):
        if not sequence:
            raise ValueError("Sequence cannot be empty")
        n = len(sequence)
        middle_index = n // 2
        return sequence[middle_index]

if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    
    middle_odd = MiddleElementFinder.find_middle(sample_sequence_odd)
    middle_even = MiddleElementFinder.find_middle(sample_sequence_even)
    
    print("Middle of odd sequence:", middle_odd)
    print("Middle of even sequence:", middle_even)