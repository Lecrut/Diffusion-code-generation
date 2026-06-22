def negate_boolean(value: bool) -> bool:
    int_val = int(value)
    flipped = int_val ^ 1
    return bool(flipped)

if __name__ == '__main__':
    result_true = negate_boolean(True)
    result_false = negate_boolean(False)
    print(result_true)
    print(result_false)