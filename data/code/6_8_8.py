def swap_spaces_for_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_input = "hello world python"
    result = swap_spaces_for_underscores(sample_input)
    print(result)