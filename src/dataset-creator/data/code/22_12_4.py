def remove_element_by_index(sequence: list | str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        del sequence[index]
    except IndexError as e:
        raise IndexError(f"Position {index} is out of range for length {len(sequence)}") from e
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_index = 2
    try:
        remove_element_by_index(sample_list, target_index)
        print(f"Updated list: {sample_list}")
        sample_string = "Hello World"
        string_index = 6
        remove_element_by_index(sample_string, string_index)
        print(f"Modified string: '{sample_string}'")
    except (TypeError, IndexError) as error:
        print(f"Error occurred: {error}")