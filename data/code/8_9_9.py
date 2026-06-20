def split_and_trim(input_string):
    parts = input_string.split(',')
    return [part.strip() for part in parts if part.strip()]

if __name__ == '__main__':
    sample_text = "  apple , banana , ,orange ,  grape  , , kiwi "
    result = split_and_trim(sample_text)
    print(result)