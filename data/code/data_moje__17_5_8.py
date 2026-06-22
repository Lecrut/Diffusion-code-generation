def get_last_element(sequence):
    if not sequence:
        raise IndexError("Empty sequence")
    return sequence[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_element(sample_list))