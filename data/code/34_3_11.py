def capitalize_words(sentence: str) -> list[str]:
    """Return a list of words with each initial letter capitalized."""
    return [word.capitalize() if word else "" for word in sentence.split()]

if __name__ == '__main__':
    sample_sentence = "hello world, this is a test."
    result = capitalize_words(sample_sentence)
    print(" ".join(result))