import re

def to_camel_case(text):
    if not text:
        return text
    if '_' not in text:
        return text
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def to_camel_case_regex(text):
    if not text or '_' not in text:
        return text
    def replace(match):
        return match.group(2).upper()
    return re.sub(r'_([a-zA-Z0-9])', replace, text)

if __name__ == '__main__':
    samples = ['snake_case_example', 'another_example_test', 'single', '_leading_trailing_', 'mixed_123_case_456']
    for sample in samples:
        print(to_camel_case_regex(sample))