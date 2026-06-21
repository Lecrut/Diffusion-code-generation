def separate_characters(input_string):
    characters = list(input_string)
    separated_chars = [char + ',' for char in characters]
    return ''.join(separated_chars[:-1])

if __name__ == '__main__':
    sample_string = "HelloWorld"
    print(separate_characters(sample_string))