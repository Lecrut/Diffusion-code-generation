def swap_spaces_for_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    result = swap_spaces_for_underscores(sample_string)
    print(result)