import re

def split_and_clean_string(s):
    if not isinstance(s, str):
        return []
    parts = s.split(',')
    cleaned = [part.strip() for part in parts if part.strip()]
    return cleaned

if __name__ == '__main__':
    sample_input = "  apple , banana , , grape ,  orange "
    result = split_and_clean_string(sample_input)
    print(result)