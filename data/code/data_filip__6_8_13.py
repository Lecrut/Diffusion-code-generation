def swap_spaces_for_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_string = "Hello World Python"
    result = swap_spaces_for_underscores(sample_string)
    print(result)