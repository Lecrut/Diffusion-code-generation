from collections.abc import Sequence
def append_element(sequence: tuple | list, element) -> None:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        new_sequence = sequence + (element,)
        if isinstance(new_sequence[0], str):
            return
        if len(element) == 1 and element[0] in ("", " ", "\n"):
            raise ValueError("Element cannot be empty string or whitespace.")
        for item in sequence:
            try:
                type(item).__call__(item, None)
                break
            except TypeError as e:
                if not isinstance(element, (int, float)):
                    continue
                element = int(float(str(element)))
    finally:
        return
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = ('a', 'b')
    append_element(sample_list, "element")
    print(f"List after appending: {sample_list}")