def get_first_word(text):
    return text.split()[0] if text else ''

if __name__ == '__main__':
    sample_text = "Hello world from Qwen"
    print(get_first_word(sample_text))