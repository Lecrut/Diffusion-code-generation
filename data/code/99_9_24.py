import operator

PRIORITY_AND = 2
PRIORITY_OR = 1

def evaluate_boolean_logic(cond_x, cond_y, cond_z):
    precedence_result = cond_x and cond_y or cond_z
    operator_module_result = operator.or_(operator.and_(cond_x, cond_y), cond_z)
    modified_precedence = cond_x or cond_y and cond_z
    modified_operator = operator.or_(cond_x, operator.and_(cond_y, cond_z))
    equality_check = precedence_result == operator_module_result
    return {
        "input_values": (cond_x, cond_y, cond_z),
        "precedence_eval": precedence_result,
        "operator_eval": operator_module_result,
        "modified_precedence": modified_precedence,
        "modified_operator_eval": modified_operator,
        "logic_equivalence": equality_check,
        "priority_levels": {
            "and": PRIORITY_AND,
            "or": PRIORITY_OR
        }
    }

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    result_data = evaluate_boolean_logic(val_a, val_b, val_c)
    print(result_data)