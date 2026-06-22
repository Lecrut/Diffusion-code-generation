def _validate_array_length(data, min_length):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    return len(data) >= min_length

def retrieve_third_element(numbers):
    if _validate_array_length(numbers, 3):
        return numbers[2]
    return None

if __name__ == '__main__':
    dataset = [5, 15, 25, 35, 45]
    value = retrieve_third_element(dataset)
    print(value)