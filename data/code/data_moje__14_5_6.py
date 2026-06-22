def _ensure_minimum_length(sequence, required_length):
    current_length = len(sequence)
    if current_length < required_length:
        raise IndexError("Sequence length is insufficient")

def get_third_item(sequence):
    _ensure_minimum_length(sequence, 3)
    return sequence[2]

if __name__ == '__main__':
    data_points = [11, 22, 33, 44, 55]
    result = get_third_item(data_points)
    print(result)
    text_data = "abcdef"
    char_result = get_third_item(text_data)
    print(char_result)
    try:
        short_data = [1, 2]
        get_third_item(short_data)
    except IndexError as error:
        print(error)