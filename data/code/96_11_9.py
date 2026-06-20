def evaluate_nested_structure(nested):
    def recursive_eval(sub_nest):
        for item in sub_nest:
            if isinstance(item, list):
                if recursive_eval(item):
                    return True
            elif item:
                return True
        return False

    return recursive_eval(nested)

if __name__ == '__main__':
    sample = [[False, [False, False]], [True, [False, False]]]
    print(evaluate_nested_structure(sample))