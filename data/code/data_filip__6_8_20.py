def swap_spaces_for_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_text = "Hello World Example"
    result = swap_spaces_for_underscores(sample_text)
    print(result)