def evaluate_or_condition(a, b):
    return (a > 5) or (b < 10)

if __name__ == '__main__':
    sample_values = {
        'a': [4, 6],
        'b': [9, 11]
    }
    
    results = {f'a={a}, b={b}': evaluate_or_condition(a, b) for a, b in zip(sample_values['a'], sample_values['b'])}
    
    for key, value in results.items():
        print(f'{key}: {value}')