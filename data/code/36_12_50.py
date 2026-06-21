def reverse_sentence(sentence):
    return sentence[::-1]

if __name__ == '__main__':
    SAMPLE_SENTENCES = [
        "Hello, World!",
        "Python is fun",
        "Alibaba Cloud"
    ]
    for original in SAMPLE_SENTENCES:
        result = reverse_sentence(original)
        print(f"Original: {original}")
        print(f"Reversed: {result}")