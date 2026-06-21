def split_string_to_words(text):
    words = text.split()
    return words

if __name__ == '__main__':
    samples = {
        "  hello world  ": ["hello", "world"],
        "multiple   spaces here": ["multiple", "spaces", "here"],
        " leading and trailing ": ["leading", "and", "trailing"],
        "singleword": ["singleword"],
        "": []
    }
    
    for sample, expected in samples.items():
        result = split_string_to_words(sample)
        print(f"Input: '{sample}'")
        print(f"Output: {result}")
        assert result == expected