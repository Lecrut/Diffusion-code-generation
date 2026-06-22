def reverse_sentence(sentence: str) -> str:
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample = "Hello world from Python"
    result = reverse_sentence(sample)
    print(result)