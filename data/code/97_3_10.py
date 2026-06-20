def print_truth_table():
    propositions = ['P', 'Q']
    truth_values = [False, True]

    for p in truth_values:
        for q in truth_values:
            implication_result = not p or q
            print(f"{p} {q} {implication_result}")

if __name__ == '__main__':
    print_truth_table()