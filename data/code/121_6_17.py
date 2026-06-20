def compare_tuples(t1, t2):
    for a, b in zip(t1, t2):
        if a > b:
            return t1
        elif a < b:
            return t2
    return t1 if len(t1) >= len(t2) else t2

if __name__ == '__main__':
    print(compare_tuples((1, 2), (3, 4)))
    print(compare_tuples((5, 6), (5, 7)))
    print(compare_tuples((8,), (9, 0)))
    print(compare_tuples(('a', 'b'), ('c', 'd')))