def evaluate_boolean_operations(a, b):
    return (a and b), (a or b), not a, not b

if __name__ == '__main__':
    sample_values = [True, False]
    results = {a: {b: evaluate_boolean_operations(a, b) for b in sample_values} for a in sample_values}
    print(results)