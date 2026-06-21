def split_text(text):
    return text.split()

if __name__ == '__main__':
    sample_string = "This is another example sentence for splitting"
    result = split_text(sample_string)
    print(result)