def extract_words(text):
    return text.split()
if __name__ == '__main__':
    sample_string = "This is a sample sentence for word extraction"
    result = extract_words(sample_string)
    print(result)