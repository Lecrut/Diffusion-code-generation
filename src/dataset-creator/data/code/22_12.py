def remove_element_at_index(container: list | str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        length = len(container)
    except TypeError as e:
        raise TypeError(f"Container does not support length operation. {e}")
    if index < 0 or index >= length:
        raise IndexError(f"Index out of range for container with length {length}.")
    del container[index]
if __name__ == '__main__':
    sample_list = [1, 'apple', 3.14, True]
    try:
        remove_element_at_index(sample_list, 2)
        print(f"Updated list: {sample_list}")
        sample_string = "hello world"
        try:
            remove_element_at_index(sample_string, 2)
            print(f"Updated string (should be unchanged): {sample_string}")
        except TypeError as te:
            pass
    except (IndexError, TypeError) as e:
        print(f"An error occurred: {e}")