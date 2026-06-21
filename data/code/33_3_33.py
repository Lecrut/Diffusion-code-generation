import string

def filter_alphanumeric(input_string):
    allowed_characters = set(string.ascii_letters + string.digits)
    filtered_chars = [char for char in input_string if char in allowed_characters]
    return ''.join(filtered_chars)

if __name__ == '__main__':
    sample_input = "Example: 3.14 and @#%!"
    result = filter_alphanumeric(sample_input)
    print(result)