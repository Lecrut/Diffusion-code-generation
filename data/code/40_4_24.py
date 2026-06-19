def find_first_letters_optimized(input_string):
    import re
    for word in re.findall(r'\b\w', input_string):
        yield word

if __name__ == '__main__':
    sample_input = "This is an example string with several words"
    result = list(find_first_letters_optimized(sample_input))
    print(result)