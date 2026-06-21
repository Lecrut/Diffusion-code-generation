def find_first_mismatch(tup1, tup2):
    for i, (a, b) in enumerate(zip(tup1, tup2)):
        if a != b:
            return i
    return -1
if __name__ == '__main__':
    sample_tup1 = (1, 2, 3, 4)
    sample_tup2 = (1, 2, 5, 4)
    print(find_first_mismatch(sample_tup1, sample_tup2))