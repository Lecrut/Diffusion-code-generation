TRUTH_TABLE_HEADERS = ['a', 'b', 'result']

def generate_truth_table(expression):
    if expression == 'single':
        inputs = [False, True]
        results = []
        for a in inputs:
            result = a
            results.append({'a': a, 'b': None, 'result': result})
        return results

    elif expression == 'two':
        inputs = [False, True]
        results = []
        for a in inputs:
            for b in inputs:
                if a and not b:
                    result = False
                elif not a and b:
                    result = True
                else:
                    result = None
                results.append({'a': a, 'b': b, 'result': result})
        return results

if __name__ == '__main__':
    single_var_table = generate_truth_table('single')
    print(single_var_table)

    two_var_table = generate_truth_table('two')
    print(two_var_table)