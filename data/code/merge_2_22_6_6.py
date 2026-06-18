def delete_by_index(sequence: list | str, index: int) -> None:
    if isinstance(sequence, str):
        sequence = list(sequence)
    try:
        del sequence[index]
    except IndexError:
        raise ValueError(f"Index {index} is out of range for the provided sequence.")
if __name__ == '__main__':
    sample_string = "hello world"
    sample_list = [10, 20, 30, 40, 50]
    delete_by_index(sample_string, 6)
    print(f"Modified string: {sample_string}")
    delete_by_index(sample_list, 2)
    print(f"Modified list: {sample_list}")