def reverse_sentence(sentence):
    words = sentence.split()
    if not words:
        return ""
    return ' '.join(words[::-1])

if __name__ == '__main__':
    sample_sentence = "Implementing efficient Python code"
    print(reverse_sentence(sample_sentence))