def get_first_element(sequence):
    if not sequence:
        raise ValueError("List must be non-empty")
    return sequence[0]

if __name__ == '__main__':
    sample_list = [42, 17, 93]
    result = get_first_element(sample_list)
    print(result)