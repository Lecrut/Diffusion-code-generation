def capitalize_words(sentence: str) -> str:
    """Capitalize the first letter of each word in the sentence."""
    return " ".join(word.capitalize() if len(word.strip()) > 0 else "" for word in sentence.split())

if __name__ == '__main__':
    sample_sentence = "hello world, this is a test."
    result = capitalize_words(sample_sentence)
    print(result)