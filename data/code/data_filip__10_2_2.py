def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_text = "This   is  a   test  string with    multiple   spaces"
    result = reverse_words(sample_text)
    print(result)