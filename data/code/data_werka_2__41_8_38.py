def case_swap(text):
    lower_text = text.lower()
    upper_text = text.upper()
    title_text = text.title()
    return {
        'lower': lower_text,
        'upper': upper_text,
        'title': title_text
    }

if __name__ == '__main__':
    sample_text = "Python Programming"
    result = case_swap(sample_text)
    print(result)