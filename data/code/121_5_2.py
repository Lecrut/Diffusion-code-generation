def size_generator(seq1, seq2):
    yield len(seq1)
    yield len(seq2)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = ['a', 'b', 'c', 'd', 'e']
    size_gen = size_generator(list_a, list_b)
    print("Iterating through sizes:")
    for size in size_gen:
        print(size)