def delete_by_index(sequence: list | str, index: int) -> None:
    if isinstance(sequence, str):
        sequence = list(sequence)
    try:
        del sequence[index]
    except IndexError:
        print(f"Index {index} out of range.")
if __name__ == '__main__':
    sample_string = "Hello World!"
    sample_list = [10, 20, 30, 40, 50]
    delete_by_index(sample_string, 7)
    print(f"Modified String: {''.join(sample_string)}")
    delete_by_index(sample_list, 2)
    print(f"Modified List: {sample_list}")