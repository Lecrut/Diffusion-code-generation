def negate_boolean_generator(values):
    result = []
    for val in values:
        if not isinstance(val, bool):
            raise ValueError(f"Expected bool, got {type(val).__name__}")
        result.append(not val)
    return result

def process_values(input_list):
    return list(negate_boolean_generator(input_list))

if __name__ == '__main__':
    sample_input = [True, True, False, False, True]
    inverted = process_values(sample_input)
    print(inverted)