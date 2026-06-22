def replace_spaces_with_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample = "Hello World This Is A Test"
    result = replace_spaces_with_underscores(sample)
    print(result)