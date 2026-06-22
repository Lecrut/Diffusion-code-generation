def case_swap(text):
    return {
        'lower': text.lower(),
        'upper': text.upper(),
        'title': text.title()
    }

if __name__ == '__main__':
    SAMPLE_TEXT = "Example Sentence"
    result = case_swap(SAMPLE_TEXT)
    print(result)