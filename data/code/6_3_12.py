import string

def replace_spaces_with_underscores(input_string):
    return input_string.replace(" ", "_")

if __name__ == '__main__':
    sample_text = "This is a sample string with spaces"
    result = replace_spaces_with_underscores(sample_text)
    print(result)