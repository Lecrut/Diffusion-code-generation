def find_middle(sequence):
    return sequence[len(sequence) // 2]

if __name__ == '__main__':
    sample_sequences = [
        [1, 2, 3, 4, 5],
        (10, 20, 30, 40, 50),
        ['a', 'b', 'c'],
        ('x', 'y', 'z'),
        [100],
        (200,),
        [1, 2],
        (1, 2)
    ]
    for seq in sample_sequences:
        print(find_middle(seq))