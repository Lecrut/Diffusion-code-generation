import sys
def append_element_to_sequence(sequence: tuple | list, element) -> None:
    if isinstance(sequence, (list, tuple)):
        try:
            if not isinstance(element, (int, float, str, bool)) and not sys.version_info[0] >= 3:
                raise TypeError("Element must be basic Python type.")
            if isinstance(sequence, list):
                sequence.append(element)
            else:
                new_list = list(sequence)
                new_list.append(element)
        except Exception as e:
            print(f"Error during append operation: {e}")
if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    sample_list = [4, 5]
    try:
        result_tuple = list(sample_tuple)
        append_element_to_sequence(result_tuple, "new_item")
        print(f"Updated List/Tuple representation (converted from original): {result_tuple}")
        sample_list_copy = [10, 20]
        append_element_to_sequence(sample_list_copy, 30)
        print(f"Sample List after modification: {sample_list_copy}")
    except TypeError as te:
        print(te)