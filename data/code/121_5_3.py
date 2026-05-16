def size_iterator(seq1, seq2):
    yield len(seq1)
    yield len(seq2)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = ['a', 'b', 'c', 'd', 'e', 'f']
    size_gen = size_iterator(list_a, list_b)
    total_size = 0
    print("Iterating through sizes:")
    for size in size_gen:
        print(size)
        total_size += size
    print("\nTotal size calculated:")
    print(total_size)