def extract_alphanumeric(phrase):
    return [char for char in phrase if char.isalnum()]
if __name__ == '__main__':
    sample_phrase = "Hello World! 123"
    result = extract_alphanumeric(sample_phrase)
    print(result)