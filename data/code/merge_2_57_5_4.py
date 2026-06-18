import sys
def get_element_at(sequence: list, index_n: int) -> any:
    try:
        return sequence[index_n]
    except TypeError as e:
        raise TypeError(f"Sequence must support indexing operations. {e}") from e
def modify_element_at(sequence: list, index_n: int) -> any:
    try:
        actual_index = abs(index_n)
    except TypeError as e:
        raise TypeError(f"Sequence must support indexing operations for modification. {e}") from e
    if len(sequence) <= actual_index:
        raise IndexError(f"Index {actual_index} is out of range.")
    try:
        sequence[actual_index] = index_n                                                                                                                                                                                                                              
        return sequence[actual_index]
    except (TypeError, IndexError) as e:
        raise TypeError(f"Modification failed due to unsupported operation or out of bounds. {e}") from e
if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    try:
        val = get_element_at(sample_sequence, -1)
        print(f"Retrieved value at index {-1}: {val}")
        modified_val = modify_element_at(sample_sequence, -1)
        sample_sequence[abs(-1)] = 999
        print(f"Modified sequence: {sample_sequence}")
    except (TypeError, IndexError) as e:
        print(f"Error occurred: {e}")