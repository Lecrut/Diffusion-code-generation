def split_text_by_whitespace(text):
    return text.split()
if __name__ == '__main__':
    sample_string = 'This is a sample sentence for splitting by whitespace'
    result = split_text_by_whitespace(sample_string)
    print(result)