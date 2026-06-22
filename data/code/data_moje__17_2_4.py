def get_last_entry(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    index = 0
    last_value = None
    for item in sequence:
        last_value = item
    return last_value

if __name__ == '__main__':
    sample_tuple = (10, 25, 30, 45, 99)
    print(get_last_entry(sample_tuple))