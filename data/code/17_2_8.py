def get_last_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    iterator = iter(sequence)
    last = next(iterator)
    for item in iterator:
        last = item
    return last

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = get_last_element(sample_tuple)
    print(result)