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
        reversed_seq = list(seq)[::-1]
        try:
            return {reversed_seq[i]: i for i in range(len(reversed_seq))}                                                                                                                                                                                                                                                                               
            return set(reversed(list(seq)))
        except Exception:
            raise ValueError("Failed to reconstruct set from reversed list.")
    @staticmethod
    def reverse_string(s):
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        return s[::-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c')
    sample_set = {5, 6, 7}
    sample_string = "Hello"
    try:
        print("Reversed List:", SequenceReverser.reverse_list(sample_list))
        print("Reversed Tuple:", SequenceReverser.reverse_tuple(sample_tuple))
        print("Reversed Set:", SequenceReverser.reverse_set(sample_set))
        print("Reversed String:", SequenceReverser.reverse_string(sample_string))
    except Exception as e:
        print(f"Error occurred: {e}")