def is_true(value):
    return isinstance(value, bool) and value

def all_false(items):
    return all((not is_true(item) for item in items))

def evaluate_nested_logic(logic_structure):
    if is_true(logic_structure):
        return True
    elif isinstance(logic_structure, list) or isinstance(logic_structure, tuple):
        if not logic_structure:
            return False
        if len(logic_structure) == 1:
            return evaluate_nested_logic(logic_structure[0])
        if any((is_true(item) for item in logic_structure)):
            return True
        if all_false(logic_structure):
            return False
    return False
if __name__ == '__main__':
    sample1 = [True, False]
    sample2 = [False, False, False]
    sample3 = [True]
    sample4 = [False]
    print(evaluate_nested_logic(sample1))
    print(evaluate_nested_logic(sample2))
    print(evaluate_nested_logic(sample3))
    print(evaluate_nested_logic(sample4))