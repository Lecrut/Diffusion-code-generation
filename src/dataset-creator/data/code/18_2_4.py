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
            if not isinstance(seq, set):
                raise TypeError("Input must be a set.")
            reversed_list = list(seq)[::-1]
            return type(seq)(reversed_list)
        except Exception as e:
            raise RuntimeError(f"Failed to reverse set due to {e}")
    @staticmethod
    def reverse_string(s):
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        return s[::-1]
if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]
    test_tuple = ('a', 'b', 'c')
    test_set = {10, 20, 30}
    test_string = "Hello World"
    print(f"Reversed List: {SequenceReverser.reverse_list(test_list)}")
    try:
        result = SequenceReverser.reverse_tuple(('x', 'y'))
        print(f"Reversed Tuple: {result}")
    except Exception as e:
        print(f"Error reversing tuple: {e}")
    try:
        reversed_set_result = SequenceReverser.reverse_set(test_set)
        print(f"Reversed Set: {reversed_set_result}")
    except Exception as e:
        print(f"Error reversing set: {e}")
    try:
        result_str = SequenceReverser.reverse_string("Python")
        print(f"Reversed String: '{result_str}'")
    except TypeError as te:
        print(te)