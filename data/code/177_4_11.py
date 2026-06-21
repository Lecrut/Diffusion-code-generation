def split_text(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return text.split()

if __name__ == '__main__':
    sample_string = "This is a sample sentence for splitting by whitespace"
    result = split_text(sample_string)
    print(result)