def reverse_sentence(sentence):
    return sentence[::-1]

if __name__ == '__main__':
    test_cases = {
        "Hello, World!": "!dlroW ,olleH",
        "Python is fun": "nuf si nohtyP",
        "Alibaba Cloud": "duolC abilibaA"
    }
    
    for original, expected in test_cases.items():
        result = reverse_sentence(original)
        print(f"Original: {original}")
        print(f"Reversed: {result}")
        assert result == expected, f"Test failed for input: {original}"