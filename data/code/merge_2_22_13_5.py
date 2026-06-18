def delete_char_at_index(sequence: str, index: int) -> str:
    if not isinstance(sequence, (str, list)):
        raise TypeError("Sequence must be a string or list.")
    try:
        length = len(sequence)
    except AttributeError:
        raise ValueError("Object does not support length calculation.")
    if index < 0 or index >= length:
        return sequence
    result_list = []
    for i, item in enumerate(sequence):
        if i != index:
            result_list.append(item)
    return ''.join(result_list)
if __name__ == '__main__':
    sample_sequence = "Hello World"
    target_index = 5
    output = delete_char_at_index(sample_sequence, target_index)
    print(output)