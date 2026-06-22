if __name__ == '__main__':
    a, b, c = 3, 1, 2
    sorted_sequence = [x for x in (a, b, c) if True]
    sorted_sequence.sort(key=lambda x: x)
    print(sorted_sequence)