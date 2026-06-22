def compare_integers(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Inputs must be integers")
    return x > y

if __name__ == '__main__':
    val_x = 15
    val_y = 25
    outcome = compare_integers(val_x, val_y)
    print(outcome)