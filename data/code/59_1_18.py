def find_middle(sequence):
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_sequences = {
        'list1': [1, 2, 3, 4, 5],
        'tuple1': (10, 20, 30, 40, 50),
        'list2': ['a', 'b', 'c'],
        'tuple2': ('x', 'y', 'z'),
        'list3': [100],
        'tuple3': (200,)
    }
    
    for name, seq in sample_sequences.items():
        print(f"{name}: {find_middle(seq)}")