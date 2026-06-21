def check_word_presence(text, target):
    words = set(text.split())
    return target in words

if __name__ == '__main__':
    sample_text = "This is a sample text for testing the word presence function."
    target_word = "sample"
    print(check_word_presence(sample_text, target_word))