def verify_integers_after_cleanup(input_str):
    translator = str.maketrans('', '', ' \t\n\r\x0b\x0c')
    cleaned = input_str.translate(translator)
    return bool(cleaned.isdigit() and cleaned)

if __name__ == '__main__':
    sample_values = ['123', '12 34', '12345\n', '123a', '', '  42  ']
    for val in sample_values:
        print(verify_integers_after_cleanup(val))