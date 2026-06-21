def strip_names(input_string):
    return [name.strip() for name in input_string.split(',')]

if __name__ == '__main__':
    sample_input = 'Alice, Bob , Charlie,  Dave'
    print(strip_names(sample_input))