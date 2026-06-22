def validate_integers(x, y):
    if not isinstance(x, int) or isinstance(x, bool):
        raise ValueError("x must be an integer")
    if not isinstance(y, int) or isinstance(y, bool):
        raise ValueError("y must be an integer")
    return True

def check_greater(x, y):
    validate_integers(x, y)
    return x > y

if __name__ == '__main__':
    val_x = 42
    val_y = 17
    outcome = check_greater(val_x, val_y)
    print(outcome)