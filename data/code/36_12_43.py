def reverse_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    return sentence[::-1]

if __name__ == '__main__':
    SAMPLE_SENTENCES = [
        "Hello, World!",
        "Python is fun",
        "Alibaba Cloud"
    ]
    
    for original in SAMPLE_SENTENCES:
        try:
            reversed_sentence = reverse_sentence(original)
            print(f"Original: {original}")
            print(f"Reversed: {reversed_sentence}")
        except ValueError as e:
            print(e)