def generate_truth_table(expression):
    if expression == 'a':
        return [{'a': False, 'result': False}, {'a': True, 'result': True}]
    elif expression == 'b':
        return [{'b': False, 'result': False}, {'b': True, 'result': True}]
    elif expression == 'a and b':
        table = []
        for a in [False, True]:
            for b in [False, True]:
                result = a and b
                table.append({'a': a, 'b': b, 'result': result})
        return table
    elif expression == 'a or b':
        table = []
        for a in [False, True]:
            for b in [False, True]:
                result = a or b
                table.append({'a': a, 'b': b, 'result': result})
        return table
    else:
        raise ValueError("Invalid expression")

if __name__ == '__main__':
    print(generate_truth_table('a'))
    print(generate_truth_table('b'))
    print(generate_truth_table('a and b'))
    print(generate_truth_table('a or b'))