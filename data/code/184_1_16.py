import re

def check_word_boundary(text, target):
    pattern = r'\b' + re.escape(target) + r'\b'
    compiled_pattern = re.compile(pattern)
    return bool(compiled_pattern.search(text))

if __name__ == '__main__':
    sample_text = "This is a test sentence for checking word boundary."
    target_word_present = "test"
    target_word_absent = "missing"
    target_word_case = "TEST"
    target_word_partial = "sentence"

    print(f"Checking '{sample_text}' for '{target_word_present}': {check_word_boundary(sample_text, target_word_present)}")
    print(f"Checking '{sample_text}' for '{target_word_absent}': {check_word_boundary(sample_text, target_word_absent)}")
    print(f"Checking '{sample_text}' for '{target_word_case}': {check_word_boundary(sample_text, target_word_case)}")
    print(f"Checking '{sample_text}' for '{target_word_partial}': {check_word_boundary(sample_text, target_word_partial)}")