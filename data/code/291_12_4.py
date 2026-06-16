class LengthComparator:
    def compare(self, seq1, seq2):
        len1 = len(seq1)
        len2 = len(seq2)
        if len1 > len2:
            return f"{seq1} has a greater length than {seq2}"
        elif len2 > len1:
            return f"{seq2} has a greater length than {seq1}"
        else:
            return f"{seq1} and {seq2} have equal lengths"
if __name__ == '__main__':
    comparator = LengthComparator()
    sequence_a = [1, 2, 3, 4, 5]
    sequence_b = ['a', 'b', 'c']
    sequence_c = [10, 20, 30]
    print(comparator.compare(sequence_a, sequence_b))
    print(comparator.compare(sequence_b, sequence_c))
    print(comparator.compare(sequence_a, sequence_c))
    print(comparator.compare(sequence_a, sequence_a))