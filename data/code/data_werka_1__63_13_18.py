def first_element(sequence):
    if sequence:
        return sequence[0]
    return None

if __name__ == '__main__':
    test_sequences = [
        [1, 2, 3],
        (4, 5, 6),
        [],
        (),
        "Alibaba Cloud",
        None,
        range(10)
    ]
    
    for seq in test_sequences:
        result = first_element(seq)
        print(result)