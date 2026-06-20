def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])

if __name__ == "__main__":
    sample_input = "  Hello   world  this  is   a test  "
    print(reverse_words(sample_input))