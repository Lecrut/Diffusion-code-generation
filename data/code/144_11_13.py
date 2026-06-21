if __name__ == '__main__':
    truth_table = '\n'.join(['A | B | A -> B', *['|'.join(map(str, row)) for row in [[a, b, a <= b] for a in [0, 1] for b in [0, 1]]]])
    print(truth_table)