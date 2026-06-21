import operator

def evaluate_boolean_logic(cond_x, cond_y, cond_z):
    standard_evaluation = cond_x and cond_y or cond_z
    explicit_parentheses = (cond_x and cond_y) or cond_z
    different_parentheses = cond_x and (cond_y or cond_z)
    operator_module_logic = operator.or_(operator.and_(cond_x, cond_y), cond_z)
    return {
        "standard": standard_evaluation,
        "explicit": explicit_parentheses,
        "different_grouping": different_parentheses,
        "operator_module": operator_module_logic
    }

if __name__ == '__main__':
    val_x = True
    val_y = False
    val_z = False
    result = evaluate_boolean_logic(val_x, val_y, val_z)
    print(result)