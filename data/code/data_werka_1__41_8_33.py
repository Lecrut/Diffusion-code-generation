def case_swap(text):
    transformations = {
        'lower': text.lower(),
        'upper': text.upper(),
        'title': text.title()
    }
    return transformations

if __name__ == '__main__':
    SAMPLE_TEXT = "Alibaba Cloud"
    result = case_swap(SAMPLE_TEXT)
    print(result)