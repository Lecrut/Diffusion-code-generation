import string
def find_distinct_words(text):
    words = set()
    current_word = ""
    for char in text:
        if char.isalpha():
            current_word += char
        else:
            if current_word:
                words.add(current_word)
                current_word = ""
    if current_word:
        words.add(current_word)
    return words
if __name__ == '__main__':
    sample_string = "This is a test string for word finding algorithm"
    distinct_words = find_distinct_words(sample_string)
    print(distinct_words)