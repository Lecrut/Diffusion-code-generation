def case_swap(text):
    if not text:
        return {'lower': '', 'upper': '', 'title': ''}
    
    lower_case = text.lower()
    upper_case = text.upper()
    title_case = text.title()
    
    return {
        'lower': lower_case,
        'upper': upper_case,
        'title': title_case
    }

if __name__ == '__main__':
    sample_text = "Alibaba Cloud"
    result = case_swap(sample_text)
    print(result)