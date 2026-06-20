def split_comma_separated_string(input_string):
    return (element.strip() for element in input_string.split(',') if element.strip())

if __name__ == '__main__':
    sample_input = "  apple , banana, ,  cherry , grape  ,  "
    result = list(split_comma_separated_string(sample_input))
    print(result)