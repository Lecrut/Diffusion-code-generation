def swap_spaces_for_underscores(input_string):
    return input_string.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "Hello World This Is A Test"
    result = swap_spaces_for_underscores(sample_text)
    print(result)