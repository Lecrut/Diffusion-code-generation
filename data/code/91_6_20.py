def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_values = {True: False, False: True}
    for key, expected in sample_values.items():
        result = negate_boolean(key)
        print(f"negate_boolean({key}) = {result}, expected {expected}")