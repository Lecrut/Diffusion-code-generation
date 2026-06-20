def negate_if_false(value):
    return not value

if __name__ == '__main__':
    print(f"False: {negate_if_false(False)}")
    print(f"True: {negate_if_false(True)}")