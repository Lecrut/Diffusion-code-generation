def evaluate_boolean_operations():
    truth_table = {(True, True): True, (True, False): False, (False, True): False, (False, False): True}

    def and_operation(a, b):
        return truth_table[a, b]

    def or_operation(a, b):
        return not truth_table[not a, not b]

    def xor_operation(a, b):
        return truth_table[a, b] != truth_table[not a, not b]
    sample_values = [(True, True), (True, False), (False, True), (False, False)]
    for a, b in sample_values:
        print(f'and({a}, {b}) = {and_operation(a, b)}')
        print(f'or({a}, {b}) = {or_operation(a, b)}')
        print(f'xor({a}, {b}) = {xor_operation(a, b)}')
if __name__ == '__main__':
    evaluate_boolean_operations()