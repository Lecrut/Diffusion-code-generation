class SequenceCounter:
    def count(self, data):
        return len(data)
if __name__ == '__main__':
    counter = SequenceCounter()
    sample_sequence_1 = [1, 2, 3, 4, 5]
    result_1 = counter.count(sample_sequence_1)
    print(f"Count for {sample_sequence_1}: {result_1}")
    sample_sequence_2 = ['a', 'b', 'c']
    result_2 = counter.count(sample_sequence_2)
    print(f"Count for {sample_sequence_2}: {result_2}")
    sample_sequence_3 = []
    result_3 = counter.count(sample_sequence_3)
    print(f"Count for {sample_sequence_3}: {result_3}")
    sample_sequence_4 = [True, False, True]
    result_4 = counter.count(sample_sequence_4)
    print(f"Count for {sample_sequence_4}: {result_4}")