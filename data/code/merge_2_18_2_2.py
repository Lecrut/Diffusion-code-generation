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
            temp_list = list(seq)
        except TypeError as e:
            raise ValueError(f"Cannot convert input to sequence. {e}") from e
        if not isinstance(temp_list, list):
            raise TypeError("Input must be a set or convertible to one.")
        return tuple(reversed(temp_list))
    @staticmethod
    def reverse_string(seq):
        try:
            string = str(seq)
        except Exception as e:
            raise ValueError(f"Cannot convert input to string. {e}") from e
        if not isinstance(string, str):
            raise TypeError("Input must be a string or convertible to one.")
        return string[::-1]
    @staticmethod
    def reverse_sequence(seq, method='auto'):
        supported_types = [list, tuple, set, str]
        detected_type = type(seq)
        if not any(detected_type in supported_types):
            raise TypeError(f"Unsupported sequence type: {detected_type.__name__}. Supported types are list, tuple, set, and string.")
        try:
            reverse_method_map = {
                'auto': detected_type,
                'list': SequenceReverser.reverse_list,
                'tuple': SequenceReverser.reverse_tuple,
                'set': SequenceReverser.reverse_set,
                'string': SequenceReverser.reverse_string
            }
            reverse_func = reverse_method_map.get(method)
            if not callable(reverse_func):
                raise ValueError(f"Invalid method specified: {method}")
            return reverse_func(seq)
        except Exception as e:
            print(f"Error during reversal: {e}")
            raise
if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], 'auto'),
        ((4, 5, 6), 'tuple'),
        ({7, 8, 9}, 'set'),
        ("hello", "string"),
        (None, None)                                                                                            
    ]
    results = []
    for seq in test_cases:
        print(f"Processing input of type {type(seq).__name__}:")
        try:
            reversed_seq = SequenceReverser.reverse_sequence(*seq)
            print(f"Result: {reversed_seq}")
            results.append(("Success", seq[0], type(reversed_seq).__name__))
        except Exception as e:
            print(f"Error with input of type {type(seq).__name__}:")
            print(e)
    try:
        invalid_input = [1, 2]
        SequenceReverser.reverse_sequence(invalid_input, method="unsupported_method")
    except Exception as e:
        print(f"Caught expected error for unsupported method: {e}")
    try:
        invalid_type = 12345
        SequenceReverser.reverse_sequence(invalid_type, method="auto")
    except Exception as e:
        print(f"Caught expected error for unsupported sequence type: {e}")