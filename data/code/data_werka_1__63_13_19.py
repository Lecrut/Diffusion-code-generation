def fetch_first_element(sequence):
    return sequence[0] if sequence else None

if __name__ == '__main__':
    test_sequences = [
        [7, 8, 9],
        (10, 11, 12),
        [],
        (),
        "world",
        None,
        456
    ]
    for seq in test_sequences:
        print(fetch_first_element(seq))