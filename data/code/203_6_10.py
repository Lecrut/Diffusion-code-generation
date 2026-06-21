def find_first_mismatch(tup1, tup2):
    for i, (a, b) in enumerate(zip(tup1, tup2)):
        if a != b:
            return i
    return -1

if __name__ == '__main__':
    result = find_first_mismatch((1, 2, 3), (1, 2, 4))
    print(result)