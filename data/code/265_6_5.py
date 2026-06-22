def extract_uppercase(phrase):
    return ''.join(char for char in phrase if char.isupper())

if __name__ == '__main__':
    sample_phrase = "Hello World!"
    print(extract_uppercase(sample_phrase))