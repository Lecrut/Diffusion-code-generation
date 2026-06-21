def negate(value):
    is_true = value is True
    is_false = value is False
    if is_true:
        result = False
    elif is_false:
        result = True
    else:
        raise ValueError("Input must be a boolean")
    return result

if __name__ == '__main__':
    sample_input = True
    output = negate(sample_input)
    print(output)
    sample_input_2 = False
    output_2 = negate(sample_input_2)
    print(output_2)