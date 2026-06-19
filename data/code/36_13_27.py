def reverse_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    return sentence[::-1]

if __name__ == '__main__':
    try:
        sample_sentence = "Qwen, Alibaba Cloud's AI"
        reversed_sentence = reverse_sentence(sample_sentence)
        print(reversed_sentence)
    except Exception as e:
        print(f"An error occurred: {e}")