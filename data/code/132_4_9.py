def negate_if_false(bool_value):
    return not bool_value

if __name__ == '__main__':
    value1 = False
    value2 = True
    print(f"negate_if_false({value1}): {negate_if_false(value1)}")
    print(f"negate_if_false({value2}): {negate_if_false(value2)}")