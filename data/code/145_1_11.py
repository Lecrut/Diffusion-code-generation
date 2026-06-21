def evaluate_nested_logic(condition_dict):
    return not (condition_dict['not'] and condition_dict['and'] or not condition_dict['or'])
if __name__ == '__main__':
    sample_values = {'not': True, 'and': False, 'or': True}
    result = evaluate_nested_logic(sample_values)
    print(result)