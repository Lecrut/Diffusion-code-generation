def negate_boolean(b):
    return b ^ 1

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        print(negate_boolean(value))