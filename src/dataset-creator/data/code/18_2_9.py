class SequenceReverser:
    @staticmethod
    def reverse_list(seq):
        if not isinstance(seq, list):
            raise TypeError("Input must be a list.")
        result = []
        for item in seq:
            try:
                reversed_item = str(item)[::-1]
                result.append(reversed_item)
            except Exception as e:
                raise RuntimeError(f"Error processing element {item}: {e}") from None
        return list(result)
    @staticmethod
    def reverse_tuple(seq):
        if not isinstance(seq, tuple):
            raise TypeError("Input must be a tuple.")
        try:
            result = []
            for item in seq:
                reversed_item = str(item)[::-1]
                result.append(reversed_item)
            return tuple(result)
        except Exception as e:
            raise RuntimeError(f"Error processing element {seq}: {e}") from None
    @staticmethod
    def reverse_set(seq):
        if not isinstance(seq, set):
            raise TypeError("Input must be a set.")
        try:
            result = []
            for item in seq:
                reversed_item = str(item)[::-1]
                result.append(reversed_item)
            return list(result)
        except Exception as e:
            raise RuntimeError(f"Error processing element {seq}: {e}") from None
    @staticmethod
    def reverse_string(seq):
        if not isinstance(seq, str):
            raise TypeError("Input must be a string.")
        try:
            return seq[::-1]
        except Exception as e:
            raise RuntimeError(f"Error processing input: {e}") from None
if __name__ == '__main__':
    test_list = [1, 2, "3", ["4"]]
    print("Reversed List:", SequenceReverser.reverse_list(test_list))
    test_tuple = (5, "6", ("7"))
    try:
        reversed_tup = SequenceReverser.reverse_tuple(test_tuple)
        print("Reversed Tuple:", reversed_tup)
    except Exception as e:
        print(f"Error with tuple: {e}")
    test_set = {"8", 9, "10"}
    try:
        reversed_set = SequenceReverser.reverse_set(test_set)
        print("Reversed Set:", reversed_set)
    except Exception as e:
        print(f"Error with set: {e}")
    test_str = "Hello World!"
    print("Reversed String:", SequenceReverser.reverse_string(test_str))
    invalid_input = [1, 2]
    try:
        result = SequenceReverser.reverse_list(invalid_input)
    except Exception:
        pass
    print("All tests completed.")