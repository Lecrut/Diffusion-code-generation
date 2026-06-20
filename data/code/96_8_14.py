def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    sample_values = {
        'a': True,
        'b': False,
        'c': True,
        'd': False
    }
    result = evaluate_expression(**sample_values)
    print(result)