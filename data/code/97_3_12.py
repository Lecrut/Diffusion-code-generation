def print_truth_table():
    propositions = ['P', 'Q']
    header = ' | '.join(propositions + [propositions[0] + ' -> ' + propositions[1]])
    separator = '-' * len(header)
    
    print(separator)
    print(header)
    print(separator)
    
    for p in [False, True]:
        for q in [False, True]:
            result = not p or q
            row = f" | ".join([str(p), str(q), str(result)])
            print(row)

if __name__ == '__main__':
    print_truth_table()