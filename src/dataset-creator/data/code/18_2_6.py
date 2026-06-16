class SequenceReverser:
    @staticmethod
    def reverse_list(seq):
        if not isinstance(seq, list):
            raise TypeError("Input must be a list.")
        return seq[::-1]
    @staticmethod
    def reverse_tuple(seq):
        if not isinstance(seq, tuple):
            raise TypeError("Input must be a tuple.")
        return seq[::-1]
    @staticmethod
    def reverse_set(seq):
        try:
            original = set(seq)
            reversed_seq = sorted(original)[::-1]
            if len(reversed_seq) != 0 and not isinstance(reversed_seq, list):
                raise TypeError("Set reversal returns a sorted list.")
            return reversed_seq
        except Exception as e:
            raise ValueError(f"Invalid input for set reversal: {e}")
    @staticmethod
    def reverse_string(seq):
        if not isinstance(seq, str):
            raise TypeError("Input must be a string.")
        return seq[::-1]
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], "list"),
        ((4, 5, 6), "tuple"),
        ({7, 8, 9}, "set"),
        ("hello", "string")
    ]
    for input_data, expected_type in test_cases:
        try:
            if isinstance(input_data, list):
                result = SequenceReverser.reverse_list(input_data)
            elif isinstance(input_data, tuple):
                result = SequenceReverser.reverse_tuple(input_data)
            elif isinstance(input_data, set):
                result = SequenceReverser.reverse_set(input_data)
            else:
                result = SequenceReverser.reverse_string(input_data)
            print(f"{expected_type}: {input_data} -> {result}")
        except Exception as ex:
            print(f"Error processing {type(input_data).__name__}: {ex}")