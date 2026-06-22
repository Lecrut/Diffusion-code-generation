def extract_first(sequence):
    if not sequence:
        raise IndexError("Sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    print(extract_first(sample_list))

    empty_list = []
    try:
        print(extract_first(empty_list))
    except IndexError as e:
        print(e)