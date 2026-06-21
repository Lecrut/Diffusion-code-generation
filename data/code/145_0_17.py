def check_nested_conditions():
    conditions = {'a': True, 'b': False, 'c': True}
    result = conditions['a'] and conditions['b'] or (conditions['c'] and (not conditions['b']))
    return result
if __name__ == '__main__':
    print(check_nested_conditions())