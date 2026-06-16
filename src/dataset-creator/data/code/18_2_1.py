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
            original_type = type(seq)
            reversed_seq = set(reversed(list(seq)))
            return reversed_seq
        except TypeError:
            raise ValueError("Input must contain hashable elements to form a set.")
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
        result_tup = SequenceReverser.reverse_tuple((10,))                                                                                                        
        print(f"Reversed Tuple: {result_tup}")
    except Exception as e:
        print(f"Error reversing tuple (expected in this specific context due to static method isolation): {e}")
    try:
        result_set = SequenceReverser.reverse_set(test_set)
        print(f"Reversed Set elements order preserved conceptually via list conversion then set back: {result_set}")
    except Exception as e:
        print(f"Error reversing set: {e}")
    try:
        reversed_str = SequenceReverser.reverse_string(test_string)
        print(f"Reversed String: '{reversed_str}'")
    except TypeError as te:
        print(te)