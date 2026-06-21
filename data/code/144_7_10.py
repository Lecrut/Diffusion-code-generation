import itertools

def generate_truth_table(variables):
    n = len(variables)
    truth_values = list(itertools.product([False, True], repeat=n))
    header = ' | '.join(variables)
    print(header)
    print('-' * (len(header) + 3))
    for row in truth_values:
        print(' | '.join(str(bit) for bit in row))

if __name__ == '__main__':
    variables = ["A", "B"]
    generate_truth_table(variables)