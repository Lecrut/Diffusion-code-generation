def transform_string(text: str) -> str:
    case_map = {'lower': 'upper', 'upper': 'lower'}
    lower_text = text.lower()
    next_case = case_map.get(lower_text[0].casefold(), 'swapcase')
    if next_case == 'lower':
        return lower_text.upper()
    elif next_case == 'upper':
        return lower_text.lower()
    else:
        return lower_text.swapcase()
if __name__ == '__main__':
    sample_string = 'Hello World'
    result = transform_string(sample_string)
    print(result)