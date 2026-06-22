def remove_spaces(input_string):
    no_space_chars = [char for char in input_string if char != " "]
    return "".join(no_space_chars)

if __name__ == '__main__':
    sample_input = "Python 3.8 is awesome!"
    result = remove_spaces(sample_input)
    print(result)