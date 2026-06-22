def evaluate_logic(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    sample_values = {
        'a': True,
        'b': False,
        'c': True,
        'd': False
    }
    result = evaluate_logic(
        sample_values['a'],
        sample_values['b'],
        sample_values['c'],
        sample_values['d']
    )
    print(result)