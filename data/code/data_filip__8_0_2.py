def split_commas(text):
    if not isinstance(text, str):
        return []
    parts = text.split(',')
    result = [p for p in parts if p]
    return result

if __name__ == '__main__':
    sample_text = "a,b,,c, d,,"
    print(split_commas(sample_text))