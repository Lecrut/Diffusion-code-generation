def split_sentence(text):
    return text.split(' ')
if __name__ == '__main__':
    sample = "Hello world this is a test"
    result = split_sentence(sample)
    print(result)
    exit(0)