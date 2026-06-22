def reverse_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    reversed_str = sentence[::-1]
    return reversed_str

if __name__ == '__main__':
    sample_sentence = "Alibaba Cloud"
    try:
        result = reverse_sentence(sample_sentence)
        print(f"Original: {sample_sentence}")
        print(f"Reversed: {result}")
    except ValueError as e:
        print(e)