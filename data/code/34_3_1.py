import string
def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)
if __name__ == '__main__':
    sample_sentence = "this is a sample sentence for testing"
    result = capitalize_words(sample_sentence)
    print(result)