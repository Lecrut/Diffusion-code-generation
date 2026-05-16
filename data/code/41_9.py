def case_swap(text):
    lower = text.lower()
    upper = text.upper()
    title = text.title()
    return {
        'lower': lower,
        'upper': upper,
        'title': title
    }
if __name__ == '__main__':
    sample_text = "Hello World Example"
    result = case_swap(sample_text)
    print(result)