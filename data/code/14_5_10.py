def get_third_item(sequence):
    if len(sequence) < 3:
        raise IndexError("Sequence must have at least three elements")
    return sequence[2]

if __name__ == '__main__':
    data_tuple = (1, 2, 3, 4, 5)
    data_string = "abcdefg"
    data_short = [1, 2]

    print(get_third_item(data_tuple))
    print(get_third_item(data_string))
    try:
        get_third_item(data_short)
    except IndexError as err:
        print(err)