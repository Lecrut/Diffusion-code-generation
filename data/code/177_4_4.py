def divide_by_whitespace(text):
    return text.split()

if __name__ == '__main__':
    sample_string = "This is a sample sentence for division"
    result = divide_by_whitespace(sample_string)
    print(result)