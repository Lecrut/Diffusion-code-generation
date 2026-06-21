def check_nested_conditions():
    expressions = {'Simple AND': True and False, 'Simple OR': True or False, 'AND with True': True and True, 'OR with False': False or False, 'Complex nested': True and (not False) or (False and True)}
    results = {key: eval(value) for key, value in expressions.items()}
    return results
if __name__ == '__main__':
    print(check_nested_conditions())