import operator

TRUE_CONST = True
FALSE_CONST = False

def evaluate_logic(X, Y, Z, W):
    bool_X = bool(X)
    bool_Y = bool(Y)
    bool_Z = bool(Z)
    bool_W = bool(W)
    first_part = operator.and_(bool_X, bool_Y)
    second_part = operator.and_(bool_Z, operator.not_(bool_W))
    final_result = operator.or_(first_part, second_part)
    return final_result

if __name__ == '__main__':
    val_X = 1
    val_Y = 0
    val_Z = 1
    val_W = 0
    result = evaluate_logic(val_X, val_Y, val_Z, val_W)
    print(result)