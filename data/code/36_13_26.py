def reverse_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    reversed_chars = [sentence[i] for i in range(len(sentence) - 1, -1, -1)]
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    try:
        reversed_sentence = reverse_sentence(sample_sentence)
        print(reversed_sentence)
    except Exception as e:
        print(f"An error occurred: {e}")