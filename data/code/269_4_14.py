def replace_punctuation(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    punctuation_marks = '.,!?;:"\'()[]{}'
    return ''.join(' ' if char in punctuation_marks else char for char in text)

if __name__ == '__main__':
    sample_string = "Hello world! How are you, today? Let's check: 123."
    result = replace_punctuation(sample_string)
    print(result)