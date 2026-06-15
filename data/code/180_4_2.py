import re
def check_words_in_text(word_list, text):
    found_words = set()
    for word in word_list:
        if re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
            found_words.add(word)
    return found_words
if __name__ == '__main__':
    sample_word_list = ["apple", "banana", "cherry", "date"]
    sample_text = "I like to eat an apple and a banana. Dates are sweet, but I prefer cherry."
    result = check_words_in_text(sample_word_list, sample_text)
    print(result)