def separate_characters(input_string):
    characters = list(input_string)
    separated_string = ','.join(characters)
    return separated_string

if __name__ == '__main__':
    sample_string = "ExampleString"
    result = separate_characters(sample_string)
    print(result)