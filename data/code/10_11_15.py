def reverse_words(sentence):
    parts = sentence.split()
    parts.reverse()
    return " ".join(parts)

if __name__ == "__main__":
    sample_input = "  Hello   world  this is   a   test  "
    result = reverse_words(sample_input)
    print(result)