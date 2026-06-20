def compare_tuples(t1, t2):
    return t1 if t1 > t2 else t2

if __name__ == '__main__':
    result = compare_tuples((3, 4), (2, 5))
    print(result)