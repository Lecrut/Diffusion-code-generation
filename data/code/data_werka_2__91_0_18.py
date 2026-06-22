def negate_boolean(value):
    if type(value) is not bool:
        raise ValueError("Argument must be of type bool")
    return value ^ True

if __name__ == '__main__':
    true_val = True
    false_val = False
    print(negate_boolean(true_val))
    print(negate_boolean(false_val))
    try:
        negate_boolean(1)
    except ValueError as e:
        print(f"Error: {e}")