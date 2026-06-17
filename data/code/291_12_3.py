class LengthComparator:
    def compare(self, seq1, seq2):
        len1 = len(seq1)
        len2 = len(seq2)
        if len1 > len2:
            return f"Sequence 1 has a greater length ({len1} vs {len2})"
        elif len2 > len1:
            return f"Sequence 2 has a greater length ({len2} vs {len1})"
        else:
            return f"Sequences have equal length ({len1})"
if __name__ == '__main__':
    comparator = LengthComparator()
    sequence_a = [1, 2, 3, 4, 5]
    sequence_b = ['a', 'b', 'c']
    sequence_c = [True, False]
    print(f"Comparing {sequence_a} and {sequence_b}: {comparator.compare(sequence_a, sequence_b)}")
    print(f"Comparing {sequence_b} and {sequence_a}: {comparator.compare(sequence_b, sequence_a)}")
    print(f"Comparing {sequence_c} and {sequence_a}: {comparator.compare(sequence_c, sequence_a)}")
    print(f"Comparing {sequence_a} and {sequence_c}: {comparator.compare(sequence_a, sequence_c)}")
    print(f"Comparing {sequence_a} and {sequence_a}: {comparator.compare(sequence_a, sequence_a)}")