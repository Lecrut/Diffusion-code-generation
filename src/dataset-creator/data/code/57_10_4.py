def get_element_indexable(data: tuple | list[int], index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        data[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds for a collection of length {len(data)}.")
        return
    result = data[index]
    if isinstance(result, (int, float)):
        print(f"The element at index {index} in the input sequence is: {result}")
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300)
    get_element_indexable(sample_list, -1)
    get_element_indexable(sample_tuple, 0)