import sys
def remove_element(data: list | str, index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        item = data[index]
    except IndexError as e:
        raise IndexError(f"Position {index} is out of range for length {len(data)}") from e
    del data[index]
def main() -> None:
    sample_list = [10, 20, 30, 40, 50]
    target_index = 2
    try:
        remove_element(sample_list, target_index)
        print(f"Updated list: {sample_list}")
    except (IndexError, TypeError) as error:
        sys.stderr.write(str(error))
if __name__ == '__main__':
    main()