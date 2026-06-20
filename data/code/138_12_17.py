def generate_truth_table(expressions):
    results = []
    for expr in expressions:
        if expr == 'a':
            table = [{'a': False, 'result': False}, {'a': True, 'result': True}]
        elif expr == 'b':
            table = [{'b': False, 'result': False}, {'b': True, 'result': True}]
        elif expr == 'a and b':
            table = [
                {'a': False, 'b': False, 'result': False},
                {'a': False, 'b': True, 'result': False},
                {'a': True, 'b': False, 'result': False},
                {'a': True, 'b': True, 'result': True}
            ]
        elif expr == 'a or b':
            table = [
                {'a': False, 'b': False, 'result': False},
                {'a': False, 'b': True, 'result': True},
                {'a': True, 'b': False, 'result': True},
                {'a': True, 'b': True, 'result': True}
            ]
        elif expr == 'not a':
            table = [{'a': False, 'result': True}, {'a': True, 'result': False}]
        elif expr == 'not b':
            table = [{'b': False, 'result': True}, {'b': True, 'result': False}]
        else:
            table = []
        results.append(table)
    return results

if __name__ == '__main__':
    expressions = ['a', 'b', 'a and b', 'a or b', 'not a', 'not b']
    tables = generate_truth_table(expressions)
    for expr, table in zip(expressions, tables):
        print(f"Truth Table for {expr}:")
        for row in table:
            print(row)