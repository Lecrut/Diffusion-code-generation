def is_any_true(value, values):
    TrueValue = True
    FalseValue = False
    lookup = {TrueValue: TrueValue, FalseValue: FalseValue}
    if lookup[value]:
        return TrueValue
    for item in values:
        if lookup[item]:
            return TrueValue
    return FalseValue

if __name__ == '__main__':
    print(is_any_true(False, [False, False, True]))
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [False, False]))