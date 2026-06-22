def remove_spaces(input_string):
    return input_string.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')

if __name__ == '__main__':
    sample_input = "This is a \tsample\nstring with \rvarying spaces."
    print(remove_spaces(sample_input))