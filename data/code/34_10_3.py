import re
def capitalize_words(text):
    words = text.split()
    capitalized_words = []
    for word in words:
        if word:
            capitalized_words.append(word[0].upper() + word[1:].lower())
        else:
            capitalized_words.append(word)
    return " ".join(capitalized_words)
if __name__ == '__main__':
    sample_string = "this is a sample string to test capitalization and mixed case"
    result = capitalize_words(sample_string)
    print(result)