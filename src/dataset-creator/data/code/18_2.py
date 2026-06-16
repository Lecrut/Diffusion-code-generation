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
            reversed_seq = list(original)[::-1]
            return tuple(reversed_seq) if isinstance(seq, (list, str)) else tuple(list(set(seq))[::-1])
        except TypeError as e:
            raise ValueError("Input must be a collection that can form a set.") from e
    @staticmethod
    def reverse_string(s):
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        return s[::-1]
if __name__ == '__main__':
    test_list = [1, 2, 3, 'a', 'b']
    test_tuple = (50, 60, 70)
    test_set_input = {40, 80}
    test_string = "Hello World"
    print(f"Reversed List: {SequenceReverser.reverse_list(test_list)}")
    try:
        result_tup = SequenceReverser.reverse_tuple(test_tuple)
        print(f"Reversed Tuple: {result_tup}")
    except Exception as e:
        print(f"Error reversing tuple: {e}")
    test_set_input_str = list({40, 80})
    try:
        result_set = SequenceReverser.reverse_set(test_set_input)
        print(f"Reversed Set (as Tuple): {result_set}")
    except Exception as e:
        print(f"Error reversing set input: {e}")
    print(f"Reversed String: '{SequenceReverser.reverse_string(test_string)}'")