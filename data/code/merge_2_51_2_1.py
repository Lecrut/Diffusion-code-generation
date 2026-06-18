def get_first_element(sequence):
    if not sequence:
        raise ValueError("Input sequence is empty")
    return sequence[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_first_element(sample_list)
    print(result)