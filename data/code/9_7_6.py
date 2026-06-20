import re

def normalize_text(text: str) -> str:
    result = text.strip()
    result = re.sub(r'\s+', ' ', result)
    return result

if __name__ == '__main__':
    sample_input = "  Hello   World  "
    normalized_output = normalize_text(sample_input)
    print(normalized_output)