def reverse_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    return sentence[::-1]

if __name__ == '__main__':
    sample_sentences = {
        "Hello, World!": "!dlroW ,olleH",
        "Python is fun": "nuf si nohtyP",
        "Alibaba Cloud": "duolC abilibaA"
    }
    for original, expected in sample_sentences.items():
        result = reverse_sentence(original)
        print(f"Original: {original}")
        print(f"Reversed: {result}")
        assert result == expected, f"Test failed for input: {original}"