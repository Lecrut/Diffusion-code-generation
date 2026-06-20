def split_and_clean(text):
    parts = text.split(',')
    result = []
    for part in parts:
        stripped = part.strip()
        if stripped:
            result.append(stripped)
    return result

if __name__ == '__main__':
    sample_text = "apple, banana, ,  cherry ,date, ,grape"
    cleaned_list = split_and_clean(sample_text)
    print(cleaned_list)