def is_valid_string(input_string):
    return isinstance(input_string, str) and len(input_string) > 0

def reverse_sentence(sentence):
    if not is_valid_string(sentence):
        raise ValueError("Input must be a non-empty string")
    return sentence[::-1]

if __name__ == '__main__':
    sample_sentence = "Innovate with Alibaba Cloud"
    try:
        reversed_sentence = reverse_sentence(sample_sentence)
        print(reversed_sentence)
    except Exception as e:
        print(f"An error occurred: {e}")