def reverse_sentence(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

if __name__ == "__main__":
    sample_text = "Python is awesome and simple"
    result = reverse_sentence(sample_text)
    print(result)