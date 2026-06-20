def split_and_trim(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    parts = text.split(',')
    result = [part.strip() for part in parts]
    result = [item for item in result if item != '']
    return result

if __name__ == '__main__':
    sample_string = "  apple , banana ,,  cherry  , , date "
    output = split_and_trim(sample_string)
    print(output)