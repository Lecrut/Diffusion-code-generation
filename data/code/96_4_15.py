def evaluate_logic(X, Y, Z, W):
    try:
        bool_X = bool(X)
        bool_Y = bool(Y)
        bool_Z = bool(Z)
        bool_W = bool(W)
    except Exception as exc:
        raise ValueError("Input conversion to boolean failed") from exc

    first_term = bool_X and bool_Y
    if first_term:
        return True

    second_term = bool_Z and (not bool_W)
    return second_term

if __name__ == '__main__':
    res = evaluate_logic(True, False, True, True)
    print(res)