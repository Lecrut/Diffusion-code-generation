HEADER_FORMAT = '{:<10} {:<10} {:<10}'

def generate_truth_table(combinations):
    print(HEADER_FORMAT.format('Input A', 'Input B', 'OR Output'))
    print('-' * 30)
    for a, b in combinations:
        or_result = a or b
        print(HEADER_FORMAT.format(a, b, or_result))
if __name__ == '__main__':
    sample_combinations = [(True, True), (True, False), (False, True), (False, False)]
    generate_truth_table(sample_combinations)