def print_truth_table():
    propositions = ['P', 'Q']
    header = ' | '.join(propositions + [f'{proposition} -> {proposition}' for proposition in propositions])
    separator = '-' * len(header)
    
    print(separator)
    print(header)
    print(separator)
    
    for p in [False, True]:
        for q in [False, True]:
            row = f' | '.join([str(p), str(q)] + [str(not q if p else True) for _ in propositions])
            print(row)

if __name__ == '__main__':
    print_truth_table()