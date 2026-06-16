def delete_by_index(sequence: list | str, index: int) -> any:
    if isinstance(sequence, str):
        return sequence[:index] + sequence[index+1:]
    try:
        new_list = list(sequence)
        del new_list[index]
        return new_list
    except IndexError:
        raise ValueError(f"Index {index} is out of range for the provided sequence.")
if __name__ == '__main__':
    sample_string = "Hello, World!"
    target_index_str = 7
    try:
        result_str = delete_by_index(sample_string, int(target_index_str))
        print(f"Modified String: {result_str}")
        sample_list = [10, 20, 30, 40, 50]
        target_index_list = 2
        result_list = delete_by_index(sample_list, int(target_index_list))
        print(f"Modified List: {result_list}")
    except ValueError as e:
        print(e)