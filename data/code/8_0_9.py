def split_commas(text):
    if text is None:
        return []
    parts = text.split(',')
    return [part for part in parts if part]

if __name__ == '__main__':
    sample_text = "apple,,banana, ,cherry,date,,,"
    result = split_commas(sample_text)
    print(result)