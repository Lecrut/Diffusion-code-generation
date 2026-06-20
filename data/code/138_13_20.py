def evaluate_boolean_operations(a, b):
    return (a and b), (a or b), not a, not b

if __name__ == '__main__':
    sample_values = [True, False]
    results = [(evaluate_boolean_operations(a, b)) for a in sample_values for b in sample_values]
    print(results)