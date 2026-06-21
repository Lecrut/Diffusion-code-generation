def check_both_false(a, b):
    if type(a) is not bool or type(b) is not bool:
        raise ValueError("Arguments must be of type bool")
    return a == False and b == False

if __name__ == '__main__':
    val_a = False
    val_b = False
    output = check_both_false(val_a, val_b)
    print(output)