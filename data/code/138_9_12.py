def generate_truth_table():
    boolean_pairs = [(False, False), (False, True), (True, False), (True, True)]
    results = {
        'AND': {pair: pair[0] and pair[1] for pair in boolean_pairs},
        'OR': {pair: pair[0] or pair[1] for pair in boolean_pairs},
        'NOT': {(False,): not False, (True,): not True},
        'XOR': {pair: pair[0] != pair[1] for pair in boolean_pairs},
        'NAND': {pair: not (pair[0] and pair[1]) for pair in boolean_pairs},
        'NOR': {pair: not (pair[0] or pair[1]) for pair in boolean_pairs},
        'IMPLIES': {(False, False): True, (False, True): True, (True, False): False, (True, True): True}
    }
    return results

if __name__ == '__main__':
    truth_table = generate_truth_table()
    print(truth_table)