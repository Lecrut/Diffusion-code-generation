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
        try:
            original_type = type(seq)
            reversed_seq = set(reversed(list(seq)))
            pass
        except TypeError:
            raise ValueError("Input must be a hashable sequence for Set.")
    @staticmethod
    def reverse_string(seq):
        if not isinstance(seq, str):
            raise TypeError("Input must be a string.")
        return seq[::-1]
def main():
    try:
        result = SequenceReverser.reverse_list([1, 2, 3])
        print(f"List reversed: {result}")
    except Exception as e:
        print(f"Error reversing list: {e}")
    try:
        result = SequenceReverser.reverse_tuple((4, 5, 6))
        print(f"Tuple reversed: {result}")
    except Exception as e:
        print(f"Error reversing tuple: {e}")
    try:
        original_set = {1, 2, 3}
        result_list = SequenceReverser.reverse_tuple(list(original_set))                                                                                               
        temp_list = list({10, 20, 30})
        reversed_temp = temp_list[::-1]
        result_set = set(reversed_temp)
        print(f"Set elements (reordered): {result_set}")                                                                         
    except Exception as e:
        print(f"Error reversing set: {e}")
    try:
        result = SequenceReverser.reverse_string("hello")
        print(f"String reversed: '{result}'")
    except Exception as e:
        print(f"Error reversing string: {e}")
if __name__ == '__main__':
    main()