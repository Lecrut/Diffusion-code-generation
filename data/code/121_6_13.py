def compare_tuples(tup1, tup2):
    return max((tup1, tup2))

if __name__ == '__main__':
    result = compare_tuples((3, 4), (2, 5))
    print(result)