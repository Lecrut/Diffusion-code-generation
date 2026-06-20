def negate_if_false(boolean_value):
    return not boolean_value

if __name__ == '__main__':
    print(f"False: {negate_if_false(False)}")
    print(f"True: {negate_if_false(True)}")