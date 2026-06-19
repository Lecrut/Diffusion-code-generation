def is_valid_sentence(sentence):
    return isinstance(sentence, str)

def reverse_sentence(sentence):
    if not is_valid_sentence(sentence):
        raise ValueError("Input must be a string")
    return sentence[::-1]

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    try:
        reversed_sentence = reverse_sentence(sample_sentence)
        print(reversed_sentence)
    except Exception as e:
        print(f"An error occurred: {e}")