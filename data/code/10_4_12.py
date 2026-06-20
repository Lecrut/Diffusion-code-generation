def reverse_word_order(text: str) -> str:
    if not text:
        return text
    words = text.split()
    words.reverse()
    return " ".join(words)

if __name__ == "__main__":
    sample_string = "Hello world this is a test"
    result = reverse_word_order(sample_string)
    print(result)