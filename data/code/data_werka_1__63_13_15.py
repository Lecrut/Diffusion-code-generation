def first_element(sequence):
    if not sequence:
        return None
    return sequence[0]

if __name__ == '__main__':
    sample_sequences = [
        [1, 2, 3],
        (4, 5, 6),
        [],
        (),
        "string",
        None,
        range(3)
    ]
    for seq in sample_sequences:
        print(first_element(seq))