def separate_characters(input_string):
    return ','.join(input_string)

if __name__ == '__main__':
    sample_string = "AdvancedProgramming"
    result = separate_characters(sample_string)
    print(result)