def reverse_word_order(text):
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    SENTENCE_MAP = {
        'demo_1': "The quick brown fox",
        'demo_2': "Python code is fun",
        'demo_3': "Reverse the order of words"
    }
    for key, value in SENTENCE_MAP.items():
        output = reverse_word_order(value)
        print(output)