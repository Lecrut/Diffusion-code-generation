import re

def group_words_by_first_letter(text):
    words = re.findall(r'\b\w+\b', text.lower())
    grouped_words = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in grouped_words:
            grouped_words[first_letter] = []
        grouped_words[first_letter].append(word)
    return grouped_words

if __name__ == '__main__':
    sample_text = "Hello world, hello Python. Welcome to the world of programming!"
    result = group_words_by_first_letter(sample_text)
    print(result)