import typing
def delete_at_index(sequence: typing.Sequence[typing.Any], index: int) -> typing.Tuple[int, ...]:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError(f"Expected a list or tuple, got {type(sequence).__name__}")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    length = len(sequence)
    if index < 0 or index >= length:
        raise IndexError(f"Index '{index}' is out of bounds for sequence of length '{length}'.")
    return tuple(seq[:index] + seq[index+1:])
if __name__ == '__main__':
    sample_list = [1, 'a', 3.5, True, None]
    target_index = 2
    try:
        result_tuple = delete_at_index(sample_list, target_index)
        print(f"Original list: {sample_list}")
        print(f"Modified tuple at index {target_index}: {result_tuple}")
        sample_string = "Hello World!"
        string_result = delete_at_index(list(sample_string), 6)
        print(f"\nOriginal string: {''.join(map(str, list(sample_string)))}")
        print(f"Modified tuple at index 6 (space removed): {string_result}")
    except Exception as e:
        if isinstance(e, TypeError):
            print(f"Type Error encountered: {e}")
        elif isinstance(e, IndexError):
            print(f"Index Error encountered: {e}")