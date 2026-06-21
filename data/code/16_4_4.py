def get_first(sequence):
    if not sequence:
        raise IndexError("Sequence is empty")
    return sequence[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_first(sample_list)
    print(result)