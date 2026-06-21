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
    for original in sample_sentences.keys():
        try:
            result = reverse_sentence(original)
            print(f"Original: {original}")
            print(f"Reversed: {result}")
            assert result == sample_sentences[original], f"Test failed for input: {original}"
        except ValueError as e:
            print(e)