def parse_comma_separated(input_string):
    return (element.strip() for element in input_string.split(',') if element.strip())

if __name__ == '__main__':
    sample_data = "  apple ,  banana,,  cherry , date "
    result = list(parse_comma_separated(sample_data))
    print(result)