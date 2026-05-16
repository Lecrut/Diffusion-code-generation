def clean_comma_separated_string(raw_string):
    if not raw_string:
        return []
    items = raw_string.split(',')
    cleaned_items = [item.strip() for item in items]
    return cleaned_items
if __name__ == '__main__':
    sample_input = " apple , banana ,cherry , date "
    result = clean_comma_separated_string(sample_input)
    print(result)