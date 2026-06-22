def invert_boolean_sequence(source):
    if not source:
        return []
    return [not val for val in source]

if __name__ == '__main__':
    data = [True, False, True, False]
    output = invert_boolean_sequence(data)
    print(output)