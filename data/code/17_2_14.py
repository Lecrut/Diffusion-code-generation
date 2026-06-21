def get_final_entry(sequence):
    if not sequence:
        raise IndexError("sequence is empty")
    iterator = iter(sequence)
    try:
        current = next(iterator)
        while True:
            current = next(iterator)
        return current
    except StopIteration:
        return current

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = get_final_entry(sample_tuple)
    print(result)