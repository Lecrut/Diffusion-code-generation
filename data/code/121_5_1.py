def sequence_size_generator(seq1, seq2):
    yield len(seq1)
    yield len(seq2)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = ['a', 'b', 'c', 'd', 'e', 'f']
    size_generator = sequence_size_generator(list_a, list_b)
    total_size = 0
    for size in size_generator:
        total_size += size
    print(f"Size of list_a: {len(list_a)}")
    print(f"Size of list_b: {len(list_b)}")
    print(f"Total size: {total_size}")