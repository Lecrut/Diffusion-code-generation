OPERATIONS = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/', 'modulus': '%'}

def perform_operations(a, b):
    results = {}
    for op, label in OPERATIONS.items():
        if op == 'divide' and b == 0:
            results[label] = None
        else:
            results[label] = eval(f'a {label} b')
    return results
if __name__ == '__main__':
    sample_values = (10, 5)
    result = perform_operations(*sample_values)
    print(result)