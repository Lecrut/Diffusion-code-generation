def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    SAMPLES = [
        ("hello world this is a test", "test a is this world hello"),
        ("optimization is key", "key is optimization"),
        ("  leading and trailing spaces   ", "spaces trailing and leading")
    ]
    
    for sample, expected in SAMPLES:
        result = reverse_words(sample)
        print(f"Input: '{sample}'")
        print(f"Output: '{result}'")
        assert result == expected, f"Expected '{expected}', but got '{result}'"