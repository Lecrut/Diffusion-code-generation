def get_middle_index(sequence):
    length = len(sequence)
    if length % 2 == 1:
        return length // 2
    else:
        return (length - 1) // 2
if __name__ == '__main__':
    test_cases = [
        ([],),
        ([5,],),
        ([1, 2, 3],),
        ([10, 20],),
        ("hello",),
        (range(6),)
    ]
    for seq in test_cases:
        print(f"Input: {seq}, Middle Index: {get_middle_index(seq)}")