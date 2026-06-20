def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == "__main__":
    text = "Hello world from Python"
    result = reverse_words(text)
    print(result)