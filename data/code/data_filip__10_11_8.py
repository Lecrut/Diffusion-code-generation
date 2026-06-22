def reverse_words(sentence: str) -> str:
    words = sentence.split()
    words.reverse()
    return " ".join(words)

if __name__ == "__main__":
    sample_sentence = "  This   is   a   test  "
    result = reverse_words(sample_sentence)
    print(result)