def evaluate_boolean_operations(a, b):
    return a and b, a or b, not a, not b

if __name__ == '__main__':
    sample_values = (True, False)
    results = [evaluate_boolean_operations(*values) for values in [(True, True), (True, False), (False, True), (False, False)]]
    print(results)