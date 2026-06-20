def print_truth_table():
    propositions = ['P', 'Q']
    header = ' | '.join(propositions) + ' | P -> Q'
    separator = '-' * len(header)

    print(separator)
    print(header)
    print(separator)

    for p in [False, True]:
        for q in [False, True]:
            implication_result = not p or q
            row = f"{p} | {q} | {implication_result}"
            print(row)

if __name__ == '__main__':
    print_truth_table()