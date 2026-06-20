def split_and_trim(text):
    parts = text.split(',')
    trimmed_parts = [part.strip() for part in parts]
    return trimmed_parts

if __name__ == '__main__':
    sample_text = "  apple,  banana ,cherry ,  "
    result = split_and_trim(sample_text)
    print(result)