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
        reversed_list = list(seq)[::-1]
        try:
            return set(reversed_list)
        except Exception as e:
            raise RuntimeError(f"Failed to convert reversed sequence back to set: {e}")
    @staticmethod
    def reverse_string(seq):
        if not isinstance(seq, str):
            raise TypeError("Input must be a string.")
        return seq[::-1]
if __name__ == '__main__':
    test_list = [1, 2, 3, 'a', 'b']
    test_tuple = (50, 60, 70)
    test_set = {40, 80}
    test_string = "Hello World"
    print(f"Reversed List: {SequenceReverser.reverse_list(test_list)}")
    try:
        result = SequenceReverser.reverse_tuple("not a tuple")
    except TypeError as e:
        print(f"Error reversing non-tuple input: {e}")
    reversed_set_result = SequenceReverser.reverse_set(test_set)
    print(f"Reversed Set: {reversed_set_result}")
    try:
        result = SequenceReverser.reverse_string(12345)
    except TypeError as e:
        print(f"Error reversing non-string input: {e}")
    reversed_str = SequenceReverser.reverse_string(test_string)
    print(f"Reversed String: '{reversed_str}'")