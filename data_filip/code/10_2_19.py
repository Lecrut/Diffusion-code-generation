def reverse_sentence_words(text):
    tokens = text.split()
    tokens.reverse()
    result = " ".join(tokens)
    return result

if __name__ == '__main__':
    original = "   The  quick   brown  fox  "
    reversed_text = reverse_sentence_words(original)
    print(reversed_text)