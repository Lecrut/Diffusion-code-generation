def xor_truth_table():
    for a in (False, True):
        for b in (False, True):
            yield (a, b, a ^ b)

if __name__ == '__main__':
    for row in xor_truth_table():
        print(row)