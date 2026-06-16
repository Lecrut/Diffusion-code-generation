def delete_character_at_index(sequence: list | str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("The 'index' parameter must be an integer.")
    if isinstance(sequence, (list, str)):
        length = len(sequence)
        if index < 0 or index >= length:
            raise IndexError(f"Index {index} is out of bounds for a sequence of size {length}.")
        if isinstance(sequence, str):
            raise TypeError("Cannot delete character from a string directly as strings are immutable. "
                           "Use slicing to create a modified copy if needed.")
        elif isinstance(sequence, list):
            del sequence[index]
    else:
        raise TypeError(f"Unsupported sequence type '{type(sequence).__name__}'. Only lists and strings are supported.")
if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    try:
        delete_character_at_index(sample_list, 1)
        print("Updated list:", sample_list)
    except (TypeError, IndexError) as e:
        print(f"Error occurred: {e}")
    test_string = "hello world"
    try:
        delete_character_at_index(test_string, 5)
    except TypeError as te:
        print("String immutability enforced:", str(te))