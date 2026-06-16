import collections
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
        if not isinstance(seq, set):
            raise TypeError("Input must be a set.")
        reversed_seq = list(reversed(list(seq)))
        try:
            return frozenset(reversed_seq)
        except Exception as e:
            raise RuntimeError(f"Failed to convert sequence back to set: {e}")
    @staticmethod
    def reverse_string(seq):
        if not isinstance(seq, str):
            raise TypeError("Input must be a string.")
        return seq[::-1]
if __name__ == '__main__':
    test_list = [1, 2, 3, 'a', 'b']
    test_tuple = (5, 6, 7)
    test_set = {4, 8, 9}
    test_string = "Hello World"
    print(f"Reversed List: {SequenceReverser.reverse_list(test_list)}")
    try:
        result = SequenceReverser.reverse_tuple("not a tuple")
    except TypeError as e:
        print(f"Caught expected error for invalid input type: {e}")
    reversed_set_result = SequenceReverser.reverse_set(test_set)
    print(f"Reversed Set (frozenset): {reversed_set_result}, Type: {type(reversed_set_result)}")
    reversed_string_result = SequenceReverser.reverse_string(test_string)
    print(f"Reversed String: '{reversed_string_result}'")