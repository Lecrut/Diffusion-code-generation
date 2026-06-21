import itertools

def build_truth_table(n):
    variables = [bool(i % 2) for i in range(n)]
    return list(itertools.product(*variables))

if __name__ == '__main__':
    sample_values = build_truth_table(3)
    print(sample_values)