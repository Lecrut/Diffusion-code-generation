def split_text_by_whitespace(text):
    return text.split()

if __name__ == '__main__':
    sample_string = "Split this string by whitespace please"
    words = split_text_by_whitespace(sample_string)
    print(words)