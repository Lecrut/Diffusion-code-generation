import sys
def capitalize_words(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)
if __name__ == '__main__':
    sample_input = "this is a sample sentence for testing"
    result = capitalize_words(sample_input)
    print(result)