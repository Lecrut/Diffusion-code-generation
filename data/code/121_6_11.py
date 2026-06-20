def compare_tuples(tup1, tup2):
    for a, b in zip(tup1, tup2):
        if a > b:
            return tup1
        elif a < b:
            return tup2
    return tup1 if len(tup1) >= len(tup2) else tup2

if __name__ == '__main__':
    print(compare_tuples((3, 4), (2, 5)))
    print(compare_tuples(('apple', 'banana'), ('banana', 'cherry')))