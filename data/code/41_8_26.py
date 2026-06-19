def case_swap(text):
    lower_case = text.lower()
    upper_case = text.upper()
    title_case = text.title()
    return {
        'lower': lower_case,
        'upper': upper_case,
        'title': title_case
    }

if __name__ == '__main__':
    sample_text = "a quick BROWN fox"
    transformation_result = case_swap(sample_text)
    print(transformation_result)