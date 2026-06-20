def generate_truth_table(expression):
    if expression == 'a':
        table = [{'a': False, 'result': False}, {'a': True, 'result': True}]
    elif expression == 'b':
        table = [{'b': False, 'result': False}, {'b': True, 'result': True}]
    elif expression == 'a and b':
        table = [{'a': False, 'b': False, 'result': False},
                 {'a': False, 'b': True, 'result': False},
                 {'a': True, 'b': False, 'result': False},
                 {'a': True, 'b': True, 'result': True}]
    elif expression == 'a or b':
        table = [{'a': False, 'b': False, 'result': False},
                 {'a': False, 'b': True, 'result': True},
                 {'a': True, 'b': False, 'result': True},
                 {'a': True, 'b': True, 'result': True}]
    elif expression == 'not a':
        table = [{'a': False, 'result': True}, {'a': True, 'result': False}]
    elif expression == 'not b':
        table = [{'b': False, 'result': True}, {'b': True, 'result': False}]
    else:
        raise ValueError("Invalid expression")
    
    return table

if __name__ == '__main__':
    print(generate_truth_table('a'))
    print(generate_truth_table('b'))
    print(generate_truth_table('a and b'))
    print(generate_truth_table('a or b'))
    print(generate_truth_table('not a'))
    print(generate_truth_table('not b'))