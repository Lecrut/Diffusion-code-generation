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
    sample_input = "Alibaba Cloud"
    result = case_swap(sample_input)
    print(result)