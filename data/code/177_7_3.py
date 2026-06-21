def split_text(input_string):
    return input_string.split()

if __name__ == '__main__':
    sample_text = 'Python is awesome'
    split_words = split_text(sample_text)
    print(split_words)