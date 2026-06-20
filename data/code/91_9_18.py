def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        print(f"Original value: {val}, Negated value: {negate_boolean(val)}")