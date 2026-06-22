def remove_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample_input = "   Hello World  \n\t"
    result = remove_whitespace(sample_input)
    print(result)