def reverse_sentence(sentence):
    return sentence[::-1]

if __name__ == '__main__':
    sample_sentences = {
        "Hello, World!": "!dlroW ,olleH",
        "Alibaba Cloud": "duolC abilibaA",
        "Efficient Python Code": "edoc nohtyP tficiffE"
    }
    
    for original, expected in sample_sentences.items():
        reversed_sentence = reverse_sentence(original)
        print(f"Original: {original}")
        print(f"Reversed: {reversed_sentence}")
        assert reversed_sentence == expected, f"Expected {expected}, but got {reversed_sentence}"