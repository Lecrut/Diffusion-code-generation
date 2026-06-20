def compare_tuples(tup1, tup2):
    return tup1 if tup1 > tup2 else tup2

if __name__ == '__main__':
    print(compare_tuples((3, 4), (1, 2)))