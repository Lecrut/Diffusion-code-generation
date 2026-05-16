def size_generator(seq1, seq2):
    yield len(seq1)
    yield len(seq2)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c']
    size_gen = size_generator(list1, list2)
    print("Iterating through sizes:")
    for size in size_gen:
        print(size)