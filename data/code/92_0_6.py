NOT_TRUE = False
TRUE = True

def negate_boolean(value):
    return not value

if __name__ == '__main__':
    sample_values = [NOT_TRUE, TRUE]
    for val in sample_values:
        print(negate_boolean(val))