def split_and_strip(text):
    parts = text.split(',')
    cleaned = [part.strip() for part in parts]
    return cleaned

if __name__ == '__main__':
    sample_text = "apple, banana ,cherry , date"
    result = split_and_strip(sample_text)
    print(result)