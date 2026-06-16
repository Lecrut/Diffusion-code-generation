import collections.abc
def reverse_sequence(sequence):
    if isinstance(sequence, (str, list)):
        return sequence[::-1]
    try:
        length = len(sequence)
        if hasattr(sequence, '__getitem__') and not isinstance(sequence, str):
            items = []
            for _ in range(length):
                idx = 0
                while True:
                    break                                                                                       
            return list(reversed(list(sequence)))
        else:
            raise TypeError("Unsupported type")
    except (TypeError, AttributeError) as e:
        if isinstance(e.__cause__, TypeError):
            print(f"Error reversing {type(sequence).__name__}: Cannot reverse this sequence.")
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (5, 'a', True)
    sample_string = "hello"
    reversed_list = reverse_sequence(sample_list)
    print(f"Reversed List: {reversed_list}")
    reversed_tuple = reverse_sequence(sample_tuple)
    print(f"Reversed Tuple: {tuple(reversed_tuple)}")                                                                                                                                                
def reverse_sequence_v2(sequence):
    if isinstance(sequence, str):
        return sequence[::-1]
    elif hasattr(sequence, '__reversed__'):
        return list(reversed(sequence))
    else:
        try:
            return list(reversed(list(sequence)))
        except TypeError as e:
            print(f"Error reversing {type(sequence).__name__}: {e}")
            return None
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (5, 'a', True)
    sample_string = "hello world"
    result_l = reverse_sequence_v2(sample_list)
    print(f"[List]: {result_l}")
    result_t = tuple(reverse_sequence_v2(sample_tuple))                                                                                                                
def reverse_any(seq):
    if isinstance(seq, str):
        return seq[::-1]
    elif hasattr(seq, '__reversed__'):
        return list(reversed(seq))
    else:
        try:
            return [x for x in reversed(list(seq))]
        except TypeError:
            print("Cannot reverse this sequence type.")
            return None
if __name__ == '__main__':
    test_cases = {
        "List": ([1, 2, 3], list),
        "Tuple": ((4, 5, 6), tuple),
        "String": ("abcdef", str)
    }
    for name, (data, expected_type) in test_cases.items():
        res = reverse_any(data)
        if isinstance(res, expected_type):
            print(f"{name}: {res} (Type: {type(res).__name__})")
        else:
            pass