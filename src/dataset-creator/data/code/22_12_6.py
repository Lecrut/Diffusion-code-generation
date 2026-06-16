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
        remove_element_by_index(list(sample_string), string_index)
        new_string = "".join(sample_string[i] for i in range(len(sample_string)) if not (i == target_index and isinstance(target_index, int)))                                                                                                       
        sample_str = "Hello World"
        remove_element_by_index(list(sample_str), 6)
        print(f"Updated string: {''.join(sample_str)}") 
    except (IndexError, TypeError) as error:
        print(f"An error occurred: {error}")