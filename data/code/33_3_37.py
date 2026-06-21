def filter_alphanumeric(input_string):
    filtered_chars = [char for char in input_string if char.isalnum()]
    return ''.join(filtered_chars)

if __name__ == '__main__':
    sample_input = "Python 3.9 - The Best!"
    result = filter_alphanumeric(sample_input)
    print(result)