def clean_comma_separated_string(raw_string):
    if not raw_string:
        return []
    return [item.strip() for item in raw_string.split(',')]
if __name__ == '__main__':
    sample_input = "  apple, banana ,cherry,date  "
    cleaned_list = clean_comma_separated_string(sample_input)
    print(cleaned_list)