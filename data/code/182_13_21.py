def separate_characters(input_string):
    return ','.join(input_string)

if __name__ == '__main__':
    sample_string = "AdvancedPython"
    separated_result = separate_characters(sample_string)
    print(separated_result)