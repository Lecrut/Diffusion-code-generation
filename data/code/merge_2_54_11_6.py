def get_center_index(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be an iterable sequence like list or tuple.")
    length = len(sequence)
    return length // 2
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = ('a', 'b', 'c')
    invalid_input = "not a sequence"
    print(f"Center of {sample_list}: ", get_center_index(sample_list))
    print(f"Center of {sample_tuple}: ", get_center_index(sample_tuple))
    try:
        result = get_center_index(invalid_input)
    except TypeError as e:
        print("Validation Error:", str(e))