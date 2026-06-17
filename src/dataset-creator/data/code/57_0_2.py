def get_or_set_value(data: list[int], index: int) -> tuple[list[int] | None, str]:
    if not isinstance(data, list):
        raise TypeError("The first argument must be a list of integers.")
    if not isinstance(index, int) and not isinstance(index, bool):
        raise TypeError(f"The second argument must be an integer index. Received: {type(index).__name__}.")
    try:
        value = data[index]
        if isinstance(value, int):
            new_data = list(data)                                                                            
            new_data[index] = value
            return new_data, f"Value {value} set at index {index}"
    except IndexError:
        raise IndexError(f"The provided index ({index}) is out of bounds for the array with length {len(data)}.")
if __name__ == '__main__':
    sample_array = [10, 20, 30]
    try:
        result_list, message = get_or_set_value(sample_array.copy(), -1)
        print(f"Operation Result: {result_list}")
        print(f"Message: {message}")
    except Exception as e:
        print(f"Error occurred: {e}")