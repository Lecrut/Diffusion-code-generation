def normalize_text(text):
    return text.strip()

if __name__ == '__main__':
    sample_data = "   Hello World   "
    result = normalize_text(sample_data)
    print(result)