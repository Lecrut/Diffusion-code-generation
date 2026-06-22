def case_swap(text):
    return {
        'lower': text.lower(),
        'upper': text.upper(),
        'title': text.title()
    }

if __name__ == '__main__':
    sample_text = "Hello World"
    result = case_swap(sample_text)
    print(result)