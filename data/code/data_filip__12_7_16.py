def clean_and_verify_integers(text):
    translation_table = str.maketrans('', '', ' \t\n\r\v\f,.:;!?@#$%^&*()[]{}|\\\'\"`~+-_=<>')
    cleaned = text.translate(translation_table)
    if cleaned == '':
        return False
    return cleaned.isdigit()

if __name__ == '__main__':
    sample_input = "123, 456! @ 789"
    result = clean_and_verify_integers(sample_input)
    print(result)