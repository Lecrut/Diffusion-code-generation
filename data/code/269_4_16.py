def replace_punctuation(text):
    punctuation_marks = '.,!?;:()"\'[]{}'
    result = ''.join(' ' if char in punctuation_marks else char for char in text)
    return result

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? Let's test this: \"it's okay.\""
    modified_string = replace_punctuation(sample_string)
    print(modified_string)