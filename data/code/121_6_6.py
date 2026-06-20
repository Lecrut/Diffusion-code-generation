def compare_tuples(t1, t2):
    return next((t for t in (t1, t2) if t > t), None)

if __name__ == '__main__':
    print(compare_tuples((1, 2), (3, 4)))
    print(compare_tuples((5, 6), (5, 7)))
    print(compare_tuples((8,), (9,)))
    print(compare_tuples(('a', 'b'), ('c', 'd')))