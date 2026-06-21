TRUTH_VALUES = [False, True]

def implication(A, B):
    return not A or B

if __name__ == '__main__':
    print('\t'.join(['A', 'B', 'A -> B']))
    for A in TRUTH_VALUES:
        for B in TRUTH_VALUES:
            result = implication(A, B)
            print(f'\t{A}\t{B}\t{result}')