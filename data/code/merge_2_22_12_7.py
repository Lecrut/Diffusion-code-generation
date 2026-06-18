def remove_by_index(sequence: list | str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        del sequence[index]
    except IndexError as e:
        raise IndexError(f"Position {index} is out of range for the given sequence." + str(e))
if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    remove_by_index(sample_list, 1)
    print("Updated list:", sample_list)