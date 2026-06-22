def reverse_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    return sentence[::-1]

if __name__ == '__main__':
    sample_sentences = [
        "Hello, World!",
        "Python is fun",
        "Alibaba Cloud"
    ]
    for original in sample_sentences:
        try:
            result = reverse_sentence(original)
            print(f"Original: {original}")
            print(f"Reversed: {result}")
        except ValueError as e:
            print(e)