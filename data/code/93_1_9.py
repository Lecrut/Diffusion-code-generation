def are_both_false(x, y):
    first_is_false = not x
    second_is_false = not y
    return first_is_false and second_is_false

if __name__ == '__main__':
    val_a = False
    val_b = False
    result = are_both_false(val_a, val_b)
    print(result)
    val_a = True
    val_b = False
    result = are_both_false(val_a, val_b)
    print(result)