def validate_integers(x, y):
    if not isinstance(x, int) or isinstance(x, bool):
        raise ValueError("x must be an integer")
    if not isinstance(y, int) or isinstance(y, bool):
        raise ValueError("y must be an integer")

def is_first_greater(x, y):
    validate_integers(x, y)
    return x > y

if __name__ == '__main__':
    val_x = 10
    val_y = 5
    outcome = is_first_greater(val_x, val_y)
    print(outcome)