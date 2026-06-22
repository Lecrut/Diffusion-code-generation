if __name__ == '__main__':
    sample_lists = [
        [0, False, None],
        [1, 2, 3],
        [],
        ['a', '', 'b'],
        [False, False, True]
    ]

    for lst in sample_lists:
        print(any(lst))