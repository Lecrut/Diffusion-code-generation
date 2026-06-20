def split_and_strip_text(text):
    parts = text.split(',')
    stripped_parts = [part.strip() for part in parts]
    return stripped_parts

if __name__ == '__main__':
    sample_text = "  apple, banana ,  cherry, date  "
    result = split_and_strip_text(sample_text)
    print(result)