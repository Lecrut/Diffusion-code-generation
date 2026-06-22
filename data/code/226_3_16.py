class SequenceFlattener:
    @staticmethod
    def flatten_sequence(input_tuple):
        return [num for num in input_tuple for _ in range(5)]

if __name__ == '__main__':
    sample_input = (1, 2, 3)
    flattened_result = SequenceFlattener.flatten_sequence(sample_input)
    print(flattened_result)