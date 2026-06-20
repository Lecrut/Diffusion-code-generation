def compare_tuples(t1, t2):
    return t1 if t1 > t2 else t2

if __name__ == '__main__':
    print(compare_tuples((3, 4), (1, 5)))
    print(compare_tuples(('apple', 'banana'), ('apple', 'cherry')))
    print(compare_tuples((10,), (9, 8, 7)))