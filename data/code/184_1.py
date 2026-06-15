def check_word_presence(text, target):
    text_lower = text.lower()
    target_lower = target.lower()
    return target_lower in text_lower
if __name__ == '__main__':
    sample_text = "This is a test sentence for checking word presence."
    target_word_present = "test"
    target_word_absent = "missing"
    target_word_case = "TEST"
    target_word_partial = "sentence"
    print(f"Checking '{sample_text}' for '{target_word_present}': {check_word_presence(sample_text, target_word_present)}")
    print(f"Checking '{sample_text}' for '{target_word_absent}': {check_word_presence(sample_text, target_word_absent)}")
    print(f"Checking '{sample_text}' for '{target_word_case}': {check_word_presence(sample_text, target_word_case)}")
    print(f"Checking '{sample_text}' for '{target_word_partial}': {check_word_presence(sample_text, target_word_partial)}")