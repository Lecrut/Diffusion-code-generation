def split_and_clean(sentence):
    tokens = sentence.split()
    cleaned_tokens = [token.strip() for token in tokens if token.strip()]
    return cleaned_tokens

if __name__ == '__main__':
    sample_sentence1 = "  I don't know where we are   "
    sample_sentence2 = "She won't go if you don't like it  "
    sample_sentence3 = "It's a test, isn't it?  "
    sample_sentence4 = "We don't care about that.  "

    print(split_and_clean(sample_sentence1))
    print(split_and_clean(sample_sentence2))
    print(split_and_clean(sample_sentence3))
    print(split_and_clean(sample_sentence4))