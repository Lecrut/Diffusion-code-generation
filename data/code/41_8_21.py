def case_swap(text):
    transformations = {
        'lower': text.lower(),
        'upper': text.upper(),
        'title': text.title()
    }
    return transformations

if __name__ == '__main__':
    sample_text = "example sentence"
    result = case_swap(sample_text)
    print(result)