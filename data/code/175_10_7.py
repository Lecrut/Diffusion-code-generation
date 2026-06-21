def split_sentence(sentence):
    return sentence.split()

if __name__ == '__main__':
    sample_sentences = [
        "  hello world  ",
        "multiple   spaces here",
        " leading and trailing ",
        ""
    ]
    
    for sentence in sample_sentences:
        result = split_sentence(sentence)
        print(f"Input: '{sentence}'")
        print(f"Output: {result}")