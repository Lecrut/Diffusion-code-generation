def find_target_word(text, target):
    words = set(text.split())
    return target in words

if __name__ == '__main__':
    sample_text = "This is a sample text for testing the function."
    target_word = "testing"
    print(find_target_word(sample_text, target_word))