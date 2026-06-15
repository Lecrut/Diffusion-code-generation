def check_word_presence(text, target):
    text_lower = text.lower()
    target_lower = target.lower()
    return target_lower in text_lower
if __name__ == '__main__':
    sample_text = "This is a test sentence for checking word presence."
    sample_target_present = "test"
    sample_target_absent = "word"
    sample_target_case = "SENTENCE"
    result1 = check_word_presence(sample_text, sample_target_present)
    print(f"'{sample_target_present}' in '{sample_text}': {result1}")
    result2 = check_word_presence(sample_text, sample_target_absent)
    print(f"'{sample_target_absent}' in '{sample_text}': {result2}")
    result3 = check_word_presence(sample_text, sample_target_case)
    print(f"'{sample_target_case}' in '{sample_text}': {result3}")